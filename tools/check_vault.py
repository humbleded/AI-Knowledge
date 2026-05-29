import argparse
import json
import re
from pathlib import Path


LINK_RE = re.compile(r"!?\[\[([^\]]+)\]\]")


def has_frontmatter(text):
    return text.startswith("---")


def resolve_link(root, source, target, markdown_files):
    target = target.split("|", 1)[0].split("#", 1)[0].strip()
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


def check(root):
    markdown_files = list(root.rglob("*.md"))
    missing_frontmatter = []
    broken_links = []
    status_counts = {}
    type_counts = {}
    raw_non_index = []

    for path in markdown_files:
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        rel = path.relative_to(root).as_posix()
        if not has_frontmatter(text):
            missing_frontmatter.append(rel)

        status = re.search(r"^status:\s*(\S+)", text, re.MULTILINE)
        note_type = re.search(r"^type:\s*(\S+)", text, re.MULTILINE)
        if status:
            status_counts[status.group(1)] = status_counts.get(status.group(1), 0) + 1
        if note_type:
            type_counts[note_type.group(1)] = type_counts.get(note_type.group(1), 0) + 1

        if rel.startswith("raw/") and not rel.endswith("/README.md") and rel != "raw/README.md":
            raw_non_index.append(rel)

        for link in LINK_RE.findall(text):
            if not resolve_link(root, path, link, markdown_files):
                broken_links.append({"file": rel, "link": link})

    return {
        "markdown_files": len(markdown_files),
        "missing_frontmatter": missing_frontmatter,
        "links": sum(len(LINK_RE.findall(p.read_text(encoding="utf-8-sig", errors="replace"))) for p in markdown_files),
        "broken_links": broken_links,
        "status_counts": dict(sorted(status_counts.items())),
        "type_counts": dict(sorted(type_counts.items())),
        "raw_non_index_files": raw_non_index,
        "has_index": (root / "index.md").exists(),
        "has_log": (root / "log.md").exists(),
        "has_agents": (root / "AGENTS.md").exists(),
    }


def main():
    parser = argparse.ArgumentParser(description="Check Obsidian/LLM wiki health.")
    parser.add_argument("--root", default=".", help="Vault root")
    parser.add_argument("--json", action="store_true", help="Print JSON")
    args = parser.parse_args()

    result = check(Path(args.root).resolve())
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    print(f"Markdown files: {result['markdown_files']}")
    print(f"Links: {result['links']}")
    print(f"Broken links: {len(result['broken_links'])}")
    print(f"Missing frontmatter: {len(result['missing_frontmatter'])}")
    print(f"Raw non-index files: {len(result['raw_non_index_files'])}")
    print(f"Statuses: {result['status_counts']}")
    if result["broken_links"]:
        print("Broken link samples:")
        for item in result["broken_links"][:20]:
            print(f"- {item['file']}: {item['link']}")


if __name__ == "__main__":
    main()
