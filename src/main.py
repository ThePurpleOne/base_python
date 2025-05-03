import numpy as np

from operations import add


def osef(a: float) -> float:
    return a + 4.2


def main():
    rng = np.random.default_rng()
    a: np.int64 = rng.integers(0, 100)
    b: np.int64 = rng.integers(0, 100)

    result = add(int(a), int(b))
    print(f"Adding {a} and {b}")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
