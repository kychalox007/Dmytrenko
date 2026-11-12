import contextlib
import io
import unittest
from decimal import Decimal

from rgr.topic_01.main import discriminant, reverse_string, string_methods
from rgr.topic_02.main import quadratic_roots, calc_if, calc_match
from rgr.topic_03.main import insertion_position
from rgr.topic_04.main import read_number, divide
from rgr.topic_05.calc import run
from rgr.topic_05.currency import convert, load_rates
from rgr.topic_05.rock_game import winner, CHOICES
from rgr.topic_07.Calculator import Calculator
from rgr.topic_07.Student import Student
from unittest.mock import Mock, patch
import sys


class RgrTests(unittest.TestCase):
    def test_reverse_and_string_methods(self):
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")
        result = string_methods("  hello PYTHON  ")
        self.assertEqual(result["strip"], "hello PYTHON")
        self.assertEqual(result["capitalize"], "  hello python  ")
        self.assertEqual(result["title"], "  Hello Python  ")
        self.assertEqual(result["upper"], "  HELLO PYTHON  ")
        self.assertEqual(result["lower"], "  hello python  ")

    def test_quadratic_cases(self):
        self.assertEqual(discriminant(1, -5, 6), 1)
        self.assertEqual(quadratic_roots(1, -5, 6), (2, 3))
        self.assertEqual(quadratic_roots(1, 2, 1), (-1,))
        self.assertEqual(quadratic_roots(1, 0, 1), ())
        self.assertEqual(quadratic_roots(0, 2, -4), (2,))
        self.assertEqual(quadratic_roots(0, 0, 1), ())
        with self.assertRaises(ValueError):
            quadratic_roots(0, 0, 0)

    def test_both_calculators(self):
        for calculator in (calc_if, calc_match):
            for operation, expected in (("+", 10), ("-", 6), ("*", 16), ("/", 4)):
                self.assertEqual(calculator(8, operation, 2), expected)
            with self.assertRaises(ValueError):
                calculator(1, "?", 2)

    def test_insertion_position(self):
        self.assertEqual(insertion_position([], 5), 0)
        for value, expected in ((0, 0), (3, 1), (4, 2), (9, 4)):
            self.assertEqual(insertion_position([1, 3, 5, 7], value), expected)

    def test_exception_input_and_zero(self):
        answers = iter(["bad", "nan", "4.5"])
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(read_number("", lambda _: next(answers)), 4.5)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_calculator_continues_and_logs_every_action(self):
        answers = iter(["?", "/", "bad", "8", "0", "+", "2", "3", "X"])
        output, log = [], []
        run(lambda _: next(answers), output.append, log.append)
        self.assertIn("Результат: 5", output)
        self.assertTrue(any("8.0 / 0.0" in message for message in log))
        self.assertTrue(any("invalid_number='bad'" in message for message in log))
        self.assertEqual(log[-1], "EXIT command")

    def test_rock_paper_scissors_all_nine_pairs(self):
        wins = {("rock", "scissor"), ("scissor", "paper"), ("paper", "rock")}
        for player in CHOICES:
            for computer in CHOICES:
                expected = ("Нічия" if player == computer else "Переміг гравець"
                            if (player, computer) in wins else "Переміг комп'ютер")
                self.assertEqual(winner(player, computer), expected)
        with self.assertRaises(ValueError):
            winner("wrong", "rock")

    def test_currency_rounding_with_control_data(self):
        # Контрольні числа тесту, а не поточні ринкові курси.
        data = [{"cc": "USD", "rate": 40.125, "exchangedate": "01.01.2000"}]
        self.assertEqual(convert("2", "usd", data)[0], Decimal("80.25"))
        for amount in ("-1", "NaN", "Infinity"):
            with self.assertRaises(ValueError):
                convert(amount, "USD", data)
        with self.assertRaises(ValueError):
            convert(1, "EUR", data)
        with self.assertRaises(ValueError):
            convert(1, "GBP", data)

    def test_requests_contract(self):
        response = Mock()
        response.json.return_value = [{"cc": "USD", "rate": 40}]
        requests = Mock()
        requests.get.return_value = response
        with patch.dict(sys.modules, {"requests": requests}):
            self.assertEqual(load_rates(), response.json.return_value)
        requests.get.assert_called_once_with(
            "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json", timeout=15)
        response.raise_for_status.assert_called_once()

    def test_oop_history_only_successful_operations(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate(2, "+", 3), 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.calculate(1, "/", 0)
        self.assertEqual(len(calculator.history), 1)
        self.assertIn("1", str(calculator))

    def test_student_special_methods_and_sort(self):
        students = [Student("Zak", 20), Student("Bob", 19)]
        self.assertEqual([s.name for s in sorted(students, key=lambda s: s.name)], ["Bob", "Zak"])
        self.assertEqual(str(students[0]), "Zak, 20 років")
        self.assertEqual(repr(students[0]), "Student('Zak', 20)")
        with self.assertRaises(ValueError):
            Student("", -1)


if __name__ == "__main__":
    unittest.main()
