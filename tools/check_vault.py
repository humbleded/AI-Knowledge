import argparse
import json
import subprocess
import sys
from pathlib import Path
import re


LINK_RE = re.compile(r"!?\[\[([^\]]+)\]\]")
STATUS_RE = re.compile(r"^status:\s*(\S+)", re.MULTILINE)
TYPE_RE = re.compile(r"^type:\s*(\S+)", re.MULTILINE)
SOURCE_URL_RE = re.compile(r"^source_url:\s*(\S+)", re.MULTILINE)

ALLOWED_NO_FRONTMATTER = {"AGENTS.md", "README.md"}
GENERATED_PATTERNS = ("__pycache__/", ".pyc", ".pyo")
CORE_INDEX_TYPES = {
    "concept-index",
    "course-index",
    "project-index",
    "paper-index",
    "global-index",
    "maintenance-log",
}


def read_text(path):
    return path.read_text(encoding="utf-8-sig", errors="replace")


def note_meta(text):
    status = STATUS_RE.search(text)
    note_type = TYPE_RE.search(text)
    source_url = SOURCE_URL_RE.search(text)
    return {
        "status": status.group(1) if status else None,
        "type": note_type.group(1) if note_type else None,
        "source_url": source_url.group(1) if source_url else None,
    }


def normalized_target(raw):
    return raw.split("|", 1)[0].split("#", 1)[0].strip()


def resolve_link(root, source, raw_target, markdown_files):
    target = normalized_target(raw_target)
    if not target or target.startswith(("http://", "https://")):
        return True

    candidates = []
    if target.startswith("/"):
        candidates.append((root / target.lstrip("/")).with_suffix(".md"))
    else:
        candidates.append((source.parent / target).with_suffix(".md"))
        candidates.append((root / target).with_suffix(".md"))
        candidates.extend(root.rglob(target + ".md"))

    if any(candidate.exists() for candidate in candidates):
        return True

    target_name = Path(target).name.lower()
    return any(path.stem.lower() == target_name for path in markdown_files)


def link_targets(text):
    return [normalized_target(link) for link in LINK_RE.findall(text)]


def is_compile_target_link(target):
    if not target:
        return False
    return any(
        target.startswith(prefix)
        or target.startswith("../" + prefix)
        or target.startswith("../../" + prefix)
        for prefix in ("01-Maps/", "02-Concepts/", "03-Courses/", "04-Projects/", "05-Papers/", "07-Reviews/")
    )


def tracked_generated_files(root):
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), "ls-files"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []

    files = []
    for line in proc.stdout.splitlines():
        path = line.replace("\\", "/")
        if any(pattern in path for pattern in GENERATED_PATTERNS):
            files.append(path)
    return files


def check(root):
    root = root.resolve()
    markdown_files = list(root.rglob("*.md"))
    index_text = read_text(root / "index.md") if (root / "index.md").exists() else ""
    log_text = read_text(root / "log.md") if (root / "log.md").exists() else ""

    errors = []
    warnings = []
    missing_frontmatter = []
    broken_links = []
    status_counts = {}
    type_counts = {}
    raw_non_index = []
    raw_without_source_url = []
    raw_without_compile_target = []
    important_not_in_index = []

    for path in markdown_files:
        text = read_text(path)
        rel = path.relative_to(root).as_posix()
        meta = note_meta(text)

        if not text.startswith("---") and rel not in ALLOWED_NO_FRONTMATTER:
            missing_frontmatter.append(rel)

        if meta["status"]:
            status_counts[meta["status"]] = status_counts.get(meta["status"], 0) + 1
        if meta["type"]:
            type_counts[meta["type"]] = type_counts.get(meta["type"], 0) + 1

        if rel.startswith("raw/") and not rel.endswith("/README.md") and rel != "raw/README.md":
            raw_non_index.append(rel)
            if meta["type"] == "source" and not meta["source_url"]:
                raw_without_source_url.append(rel)
            if not any(is_compile_target_link(target) for target in link_targets(text)):
                raw_without_compile_target.append(rel)

        if meta["type"] in CORE_INDEX_TYPES or meta["status"] in {"usable", "pass"}:
            rel_no_ext = rel[:-3] if rel.endswith(".md") else rel
            if rel_no_ext not in index_text and Path(rel).stem not in index_text:
                important_not_in_index.append(rel)

        for link in LINK_RE.findall(text):
            if not resolve_link(root, path, link, markdown_files):
                broken_links.append({"file": rel, "link": link})

    if not (root / "index.md").exists():
        errors.append("missing index.md")
    if not (root / "log.md").exists():
        errors.append("missing log.md")
    if not (root / "AGENTS.md").exists():
        errors.append("missing AGENTS.md")
    if broken_links:
        errors.append(f"{len(broken_links)} broken wikilinks")
    if missing_frontmatter:
        errors.append(f"{len(missing_frontmatter)} markdown files missing frontmatter")

    tracked_generated = tracked_generated_files(root)
    if tracked_generated:
        errors.append(f"{len(tracked_generated)} generated files are tracked by git")

    if raw_without_source_url:
        warnings.append(f"{len(raw_without_source_url)} raw source notes missing source_url")
    if raw_without_compile_target:
        warnings.append(f"{len(raw_without_compile_target)} raw notes missing compile target links")
    if important_not_in_index:
        warnings.append(f"{len(important_not_in_index)} important notes not referenced by index.md")
    if "check_vault.py" not in log_text:
        warnings.append("log.md does not mention check_vault.py")

    total_links = sum(len(LINK_RE.findall(read_text(path))) for path in markdown_files)
    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "markdown_files": len(markdown_files),
        "links": total_links,
        "broken_links": broken_links,
        "missing_frontmatter": missing_frontmatter,
        "status_counts": dict(sorted(status_counts.items())),
        "type_counts": dict(sorted(type_counts.items())),
        "raw_non_index_files": raw_non_index,
        "raw_without_source_url": raw_without_source_url,
        "raw_without_compile_target": raw_without_compile_target,
        "important_not_in_index": important_not_in_index,
        "tracked_generated_files": tracked_generated,
        "has_index": (root / "index.md").exists(),
        "has_log": (root / "log.md").exists(),
        "has_agents": (root / "AGENTS.md").exists(),
    }


def print_text(result):
    print(f"OK: {result['ok']}")
    print(f"Markdown files: {result['markdown_files']}")
    print(f"Links: {result['links']}")
    print(f"Broken links: {len(result['broken_links'])}")
    print(f"Missing frontmatter: {len(result['missing_frontmatter'])}")
    print(f"Raw non-index files: {len(result['raw_non_index_files'])}")
    print(f"Statuses: {result['status_counts']}")

    if result["errors"]:
        print("Errors:")
        for item in result["errors"]:
            print(f"- {item}")

    if result["warnings"]:
        print("Warnings:")
        for item in result["warnings"]:
            print(f"- {item}")

    if result["broken_links"]:
        print("Broken link samples:")
        for item in result["broken_links"][:20]:
            print(f"- {item['file']}: {item['link']}")


def main():
    parser = argparse.ArgumentParser(description="Check Obsidian/LLM wiki health.")
    parser.add_argument("--root", default=".", help="Vault root")
    parser.add_argument("--json", action="store_true", help="Print JSON")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero on warnings as well as errors")
    args = parser.parse_args()

    result = check(Path(args.root))
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_text(result)

    if result["errors"] or (args.strict and result["warnings"]):
        sys.exit(1)


if __name__ == "__main__":
    main()
