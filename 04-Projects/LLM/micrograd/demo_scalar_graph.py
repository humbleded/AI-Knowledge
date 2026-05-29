from engine import Value


def main():
    a = Value(2.0, label="a")
    b = Value(-3.0, label="b")
    c = Value(10.0, label="c")
    d = a * b + c
    d.label = "d"
    e = d.tanh()
    e.label = "e"
    e.backward()

    for name, value in [("a", a), ("b", b), ("c", c), ("d", d), ("e", e)]:
        print(f"{name}: data={value.data:.6f}, grad={value.grad:.6f}")


if __name__ == "__main__":
    main()
