import time

start = time.perf_counter_ns()
import numpy as np

print(f"Import time: {(time.perf_counter_ns() - start) / 1_000_000} ms")


def add(
    a: int,
    b: int,
) -> int:
    """
    Simple demo type hinting function
    """

    return a + b


def main():
    a: int = np.random.randint(0, 100)
    b: int = np.random.randint(0, 100)

    print(f"Adding {a} and {b}")
    print(f"Result: {add(a, b)}")


if __name__ == "__main__":
    main()
