"""Розв'язання завдань про рядки та квадратне рівняння."""


def reverse_string(text: str) -> str:
    """Повертає рядок у зворотному порядку."""
    return text[::-1]


def discriminant(a: float, b: float, c: float) -> float:
    """Обчислює дискримінант квадратного рівняння ax² + bx + c = 0."""
    return b**2 - 4 * a * c


def main() -> None:
    sample = "Hello, Python!"
    print("Рядок у зворотному порядку:", reverse_string(sample))

    a, b, c = 1, -3, 2
    print(f"Дискримінант рівняння {a}x² + ({b})x + ({c}) = 0:", discriminant(a, b, c))


if __name__ == "__main__":
    main()
