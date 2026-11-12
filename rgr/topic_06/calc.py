"""Тема 6. Логування введення, операцій, результатів і помилок."""
import argparse
from datetime import datetime
from pathlib import Path
from rgr.topic_05.calc import run


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", type=Path, default=Path("calculator.log"))
    args = parser.parse_args()
    with args.log.open("a", encoding="utf-8") as stream:
        def log(message):
            stream.write(f"{datetime.now().isoformat(timespec='seconds')} {message}\n")
            stream.flush()
        run(log=log)
    print("Журнал:", args.log)


if __name__ == "__main__":
    main()
