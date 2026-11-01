"""Топік 1: обернення рядка."""


def reverse_string(text: str) -> str:
    """Повертає рядок у зворотному порядку."""
    return text[::-1]


if __name__ == "__main__":
    sample = "Hello, Python!"
    print("Початковий рядок:", sample)
    print("Рядок навпаки:", reverse_string(sample))
