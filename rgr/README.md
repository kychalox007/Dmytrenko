# Розрахунково-графічна робота

Дмитренко Ігор Євгенійович, КБ-252. Технології програмування, 2026.
Запускати команди з кореня репозиторію Dmytrenko, Python 3.10+.

| Тема | Запуск |
| --- | --- |
| 1 Рядки та дискримінант | `python -m rgr.topic_01.main` |
| 2 Корені та калькулятори if і match | `python -m rgr.topic_02.main --demo` (без --demo інтерактивний калькулятор) |
| 3 Цикли, списки, словники | `python -m rgr.topic_03.main --demo` (без --demo циклічний калькулятор) |
| 4 Винятки | `python -m rgr.topic_04.main` |
| 5 Гра | `python -m rgr.topic_05.rock_game` |
| 5 Конвертер | `python -m rgr.topic_05.currency` |
| 5 Модульний калькулятор | `python -m rgr.topic_05.calc` |
| 6 Логування | `python -m rgr.topic_06.calc --log calculator.log` |
| 6 Сортування словників | `python -m rgr.topic_06.sorting` |
| 7 Student і калькулятор ООП | `python -m rgr.topic_07.main --demo` (без --demo інтерактивний калькулятор) |

Залежності: `python -m pip install -r requirements.txt`.
Для онлайн-запиту НБУ використовується requests; потрібне з'єднання з інтернетом.
Програма показує дату курсу і не підмінює його збереженими даними автоматично.

Для відтворення розрахунків зі знімка відповіді НБУ за 12.11.2026:

`python -m rgr.topic_05.currency --rates-json rgr/topic_05/nbu_rates_2026-11-12.json`

У JSON збережені лише три потрібні валюти з відповіді
https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json.
Кількість валюти множиться на курс, округлення до копійок виконує Decimal.

Тести: `python -m unittest rgr.test_rgr -v`.
Це 11 тестових методів; перевірка гри перебирає всі дев'ять пар ходів.
HTTP-контракт requests перевіряється з підміною сервісу, без зовнішнього запиту.

Документація:
https://docs.python.org/3/library/exceptions.html
https://docs.python.org/3/tutorial/classes.html
