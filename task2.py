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


def percent(tota, num):
    return (100 * num) / tota


def quantity_of_words(queries):
    words_quantity = list()
    counter = {}

    for string in queries:
        words_quantity.append(len(string.split()))

    for elem in words_quantity:
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


    for key, value in quantity_of_words(queries).items():
        print(f"Search queries containing {key} word(s):{round(percent(len(queries), value), 2)}%")
