"""A tiny calculator/math utility library.

This is intentionally simple — the point of this project is to practice
CI/CD with GitHub Actions, not to build a complex app.
"""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Cannot compute factorial of a negative number")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("10 / 2 =", divide(10, 2))
    print("Is 7 prime?", is_prime(7))
    print("5! =", factorial(5))
