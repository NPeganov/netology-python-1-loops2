"""
Задание 5 (необязательно)
Дан список произвольной длины. Необходимо написать код, который на основе исходного списка составит словарь такого
уровня вложенности, какова длина исходного списка.

Примеры работы программы:

my_list = ['2018-01-01', 'yandex', 'cpc', 100]
Результат: {'2018-01-01': {'yandex': {'cpc': 100}}}

my_list = ['a', 'b', 'c', 'd', 'e', 'f']
Результат: {'a': {'b': {'c': {'d': {'e': 'f'}}}}}

"""


def create_a_dict(my_list):
    dictionary = my_list[-1]  # Прихраниваем значение самого "глубокого" элемента
    for key in reversed(my_list[:-1]):
        dictionary = {key: dictionary}  # Собираем словарь

    return dictionary


if __name__ == '__main__':
    input_list = ['linux', 'ubuntu', 'fedora', 'windows']  # Как пример, но работает с любым

    print(create_a_dict(input_list))
