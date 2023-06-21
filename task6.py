"""
Задание 6 (необязательно)
Дана книга рецептов с информацией о том, сколько ингредиентов нужно для приготовления блюда в расчете на одну порцию
(пример данных представлен ниже).
Напишите программу, которая будет запрашивать у пользователя количество порций для приготовления этих блюд и отображать
информацию о суммарном количестве требуемых ингредиентов в указанном виде.
Внимание! Одинаковые ингредиенты с разными размерностями нужно считать раздельно!
Пример работы программы:

cook_book = {
  'салат': [
     {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
     {'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
     {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
     {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
    ],
  'пицца': [
     {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
     {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
     {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
    ],
  'лимонад': [
     {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
     {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
     {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
    ]
}

Введите количество порций:
3
Результат:

Сыр: 210 гр
Томаты: 6 шт
Огурцы: 60 гр
Маслины: 30 гр
Оливковое масло: 60 мл
Салат: 30 гр
Перец: 60 гр
Колбаса: 90 гр
Бекон: 90 гр
Оливки: 30 гр
Томаты: 60 гр
Тесто: 300 гр
Лимон: 3 шт
Вода: 600 мл
Сахар: 30 гр
Лайм: 60 гр

"""

from common.positive_digital_input import positive_digital_input


def uniqify_ingridients(cook_book):
    # Формируем новый словарь, где ключом является кортеж, в котором первый элемент - название ингридиента, а второй -
    # единица измерения, а значением является количество
    NAME = 'ingridient_name'
    MEASURE = 'measure'
    QUANTITY = 'quantity'
    result_dict = {}
    for recipe in cook_book.values():
        for ingridient in recipe:
            name = ingridient[NAME]
            measure = ingridient[MEASURE]
            name_and_measure = (name, measure)
            quantity = ingridient[QUANTITY]
            # Делаем проверку на повторение ингредиента в переменной
            if name_and_measure not in result_dict:
                result_dict[name_and_measure] = quantity
            else:
                result_dict[name_and_measure] += quantity

    return result_dict


def qnty_calc(multiplier, ingridients_dict):
    for _ in ingridients_dict:
        ingridients_dict[_] *= multiplier

    return ingridients_dict


def output(result_dict):
    result_string = str()
    for name_and_measure_key, value in result_dict.items():
        name, measure = name_and_measure_key
        result_string += f"{name.capitalize()}: {value} {measure} \n"
    return result_string


if __name__ == '__main__':
    cook_book = {
      'салат': [
         {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
         {'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
         {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
         {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
         {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
         {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
         {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
        ],
      'пицца': [
         {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
         {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
         {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
         {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
         {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
         {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
        ],
      'лимонад': [
         {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
         {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
         {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
         {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
        ]
    }

    persons = positive_digital_input('Enter the quantity of persons: ')
    print(output(qnty_calc(persons, uniqify_ingridients(cook_book))))
