"""Топік 3: обчислення дискримінанта квадратного рівняння."""


def discriminant(a: float, b: float, c: float) -> float:
    """Обчислює D = b² - 4ac для рівняння ax² + bx + c = 0."""
    return b**2 - 4 * a * c


if __name__ == "__main__":
    a, b, c = 1, -3, 2
    print("Дискримінант:", discriminant(a, b, c))
