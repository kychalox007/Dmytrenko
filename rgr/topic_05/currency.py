"""Курси НБУ через requests. Знімок JSON дозволяє повторити обчислення офлайн."""
import argparse
import json
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path

API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
SUPPORTED = {"EUR", "USD", "PLN"}


def load_rates():
    import requests  # pip install -r requirements.txt
    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()
    return response.json()


def convert(amount, currency, rates):
    currency = currency.strip().upper()
    if currency not in SUPPORTED:
        raise ValueError("Підтримуються EUR, USD, PLN")
    amount = Decimal(str(amount))
    if not amount.is_finite() or amount < 0:
        raise ValueError("Кількість має бути невід'ємним скінченним числом")
    record = next((row for row in rates if row.get("cc") == currency), None)
    if record is None:
        raise ValueError(f"НБУ не повернув курс {currency}")
    rate = Decimal(str(record["rate"]))
    if not rate.is_finite() or rate <= 0:
        raise ValueError("Некоректний курс НБУ")
    result = (amount * rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return result, rate, record["exchangedate"]


def main():
    parser = argparse.ArgumentParser(description="Конвертація EUR, USD, PLN у гривні")
    parser.add_argument("--rates-json", type=Path,
                        help="Збережена відповідь НБУ для відтворення прикладу офлайн")
    args = parser.parse_args()
    try:
        amount = input("Кількість валюти: ").strip().replace(",", ".")
        currency = input("EUR, USD або PLN: ").strip().upper()
        rates = (json.loads(args.rates_json.read_text(encoding="utf-8"))
                 if args.rates_json else load_rates())
        result, rate, date = convert(amount, currency, rates)
        print(f"Дата курсу НБУ: {date}")
        print(f"{amount} {currency} x {rate} = {result} UAH")
        if args.rates_json:
            print("Режим відтворення зі збереженої відповіді НБУ")
    except ImportError:
        parser.exit(1, "Встановіть залежність: pip install -r requirements.txt\n")
    except (ValueError, InvalidOperation, KeyError, TypeError, OSError) as error:
        parser.exit(1, f"Помилка: {error}\n")
    except Exception as error:
        # requests має власні винятки мережі, HTTP та декодування JSON.
        import requests
        if isinstance(error, requests.RequestException):
            parser.exit(1, f"Не вдалося отримати курс НБУ: {error}\n")
        raise


if __name__ == "__main__":
    main()
