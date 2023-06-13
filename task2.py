"""
Задание 2
Дана переменная, в которой хранится список поисковых запросов пользователя (пример структуры данных приведен ниже, но
запросы потенциально могут быть любые). Вам необходимо написать программу, которая выведет на экран распределение
количества слов в запросах в требуемом виде.

Пример работы программы:

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]
Результат:

Поисковых запросов, содержащих 2 слов(а): 42.86%
Поисковых запросов, содержащих 3 слов(а): 57.14%
"""


def percent(total, num):
    # Считаем проценты
    return (100 * num) / total


def quantity_of_words(queries):
    words_quantity = list()
    counter = {}

    for string in queries:
        # Считаем кол-во слов в строке
        words_quantity.append(len(string.split()))

    for elem in words_quantity:
        # Получаем словарь с количеством слов в одной строке в качестве ключа
        # и количеством строк с этим количеством слов в качестве значения
        counter[elem] = counter.get(elem, 0) + 1

    return counter


if __name__ == '__main__':
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт',
    ]

    for key, value in sorted(quantity_of_words(queries).items()):
        # Используем sorted(), чтобы отсортировать словарь по ключам
        # Функция round() используется для округления, чтобы дробь не была слишком длинной
        result = round(percent(len(queries), value), 2)
        print(f"Search queries containing {key} word(s): {result}%")
