import numpy as np

from operations import add, subtract


def osef(a: float) -> float:
    return a + 4.2


def main():
    rng = np.random.default_rng()
    a: np.int64 = rng.integers(0, 100)
    b: np.int64 = rng.integers(0, 100)

    result = add(int(a), int(b))
    print(f"Adding {a} and {b}")
    print(f"Addition Result: {result}")

    subtraction_result = subtract(int(b), int(a))
    print(f"Subtracting {a} from {b}")
    print(f"Subtraction Result: {subtraction_result}")


if __name__ == "__main__":
    main()
