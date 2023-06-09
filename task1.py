"""

Задание 1
Дана переменная, в которой хранится словарь, содержащий гео-метки для каждого пользователя (пример структуры данных
приведен ниже). Вам необходимо написать программу, которая выведет на экран множество уникальных гео-меток всех
пользователей.

Пример работы программы:

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
Результат: {98, 35, 15, 213, 54, 119}

"""


def unic_geo_tags(geo_tags):
    vals = geo_tags.values()
    result = []
    for v in vals:
        result.extend(v)

    return set(result)


if __name__ == '__main__':
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    print(f"Result: {unic_geo_tags(ids)}")
