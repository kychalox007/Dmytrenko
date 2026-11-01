def reverse_string(text: str) -> str:
    return text[::-1]


def discriminant(a: float, b: float, c: float) -> float:
    return b**2 - 4 * a * c


if __name__ == "__main__":
    sample = "Hello, Python!"
    print(reverse_string(sample))
    print(discriminant(1, -3, 2))
