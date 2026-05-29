import random

from nn import MLP


def main():
    random.seed(42)
    xs = [
        [2.0, 3.0, -1.0],
        [3.0, -1.0, 0.5],
        [0.5, 1.0, 1.0],
        [1.0, 1.0, -1.0],
    ]
    ys = [1.0, -1.0, -1.0, 1.0]
    model = MLP(3, [4, 4, 1])
    learning_rate = 0.05
    losses = []

    for step in range(60):
        ypred = [model(x) for x in xs]
        loss = sum((yout - ygt) ** 2 for ygt, yout in zip(ys, ypred))

        for p in model.parameters():
            p.grad = 0.0
        loss.backward()

        for p in model.parameters():
            p.data += -learning_rate * p.grad

        losses.append(loss.data)
        if step in {0, 1, 2, 9, 19, 39, 59}:
            print(f"step={step:02d} loss={loss.data:.6f}")

    print("predictions=" + ", ".join(f"{model(x).data:.3f}" for x in xs))
    print(f"loss_start={losses[0]:.6f}")
    print(f"loss_end={losses[-1]:.6f}")


if __name__ == "__main__":
    main()
