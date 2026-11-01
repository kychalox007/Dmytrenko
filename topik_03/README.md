# Топік 3

1. Калькулятор повторює введення чисел та операцій, доки не отримує команду `exit`.
2. Тести перевіряють методи списків `extend()`, `append()`, `insert()`, `remove()`, `clear()`, `sort()`, `reverse()` і `copy()`.
3. Тести перевіряють методи словників `update()`, `del`, `clear()`, `keys()`, `values()` і `items()`.
4. Функція `find_insertion_position()` знаходить індекс для вставки елемента у відсортований список.

Запускати з кореневої папки репозиторію:

```bash
python -m topik_03.calculator_loop
python -m unittest topik_03.test_list_methods -v
python -m unittest topik_03.test_dict_methods -v
python -m unittest topik_03.test_sorted_insert -v
```
