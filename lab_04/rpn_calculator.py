import re

TOKEN_PATTERN = re.compile(r"(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?|[()+\-*/^]")
NUMBER_PATTERN = re.compile(r"(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?")
PRECEDENCE = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "u+": 3,
    "u-": 3,
    "^": 4,
}
RIGHT_ASSOCIATIVE = {"^", "u+", "u-"}


def tokenize(expression):
    tokens = []
    position = 0

    for match in TOKEN_PATTERN.finditer(expression):
        if expression[position:match.start()].strip():
            raise ValueError("Вираз містить невідомий символ")

        tokens.append(match.group())
        position = match.end()

    if expression[position:].strip():
        raise ValueError("Вираз містить невідомий символ")
    if not tokens:
        raise ValueError("Вираз порожній")

    return tokens


def to_rpn(expression):
    output = []
    operators = []
    expect_operand = True

    for token in tokenize(expression):
        if NUMBER_PATTERN.fullmatch(token):
            if not expect_operand:
                raise ValueError("Між операндами має бути оператор")
            output.append(token)
            expect_operand = False
        elif token == "(":
            if not expect_operand:
                raise ValueError("Між операндами має бути оператор")
            operators.append(token)
        elif token == ")":
            if expect_operand:
                raise ValueError("Некоректний вираз у дужках")

            while operators and operators[-1] != "(":
                output.append(operators.pop())

            if not operators:
                raise ValueError("Не вистачає відкривальної дужки")

            operators.pop()
            expect_operand = False
        else:
            if expect_operand:
                if token not in {"+", "-"}:
                    raise ValueError("Після оператора має бути операнд")
                operators.append("u" + token)
                continue

            while operators and operators[-1] != "(":
                top = operators[-1]
                should_pop = PRECEDENCE[top] > PRECEDENCE[token]
                same_precedence = PRECEDENCE[top] == PRECEDENCE[token]
                if should_pop or (same_precedence and token not in RIGHT_ASSOCIATIVE):
                    output.append(operators.pop())
                else:
                    break

            operators.append(token)
            expect_operand = True

    if expect_operand:
        raise ValueError("Вираз не може завершуватися оператором")

    while operators:
        operator = operators.pop()
        if operator == "(":
            raise ValueError("Не вистачає закривальної дужки")
        output.append(operator)

    return output


def evaluate_rpn(tokens):
    stack = []

    for token in tokens:
        if NUMBER_PATTERN.fullmatch(token):
            stack.append(float(token))
        elif token in {"u+", "u-"}:
            if not stack:
                raise ValueError("Некоректний зворотний польський запис")
            value = stack.pop()
            stack.append(value if token == "u+" else -value)
        elif token in {"+", "-", "*", "/", "^"}:
            if len(stack) < 2:
                raise ValueError("Некоректний зворотний польський запис")

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            elif token == "/":
                if right == 0:
                    raise ZeroDivisionError("Ділення на нуль")
                stack.append(left / right)
            else:
                stack.append(left ** right)
        else:
            raise ValueError("Невідомий елемент зворотного польського запису")

    if len(stack) != 1:
        raise ValueError("Некоректний зворотний польський запис")

    return stack[0]


def calculate_expression(expression):
    rpn = to_rpn(expression)
    return rpn, evaluate_rpn(rpn)


def format_result(value):
    if isinstance(value, complex):
        return str(value)
    if value.is_integer():
        return str(int(value))
    return format(value, ".12g")


def main():
    expression = input("Введіть математичний вираз: ")

    try:
        rpn, result = calculate_expression(expression)
        print("Зворотний польський запис:", " ".join(rpn))
        print("Результат:", format_result(result))
    except (ValueError, ZeroDivisionError, OverflowError) as error:
        print("Помилка:", error)


if __name__ == "__main__":
    main()
