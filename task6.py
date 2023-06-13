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

    person = int(input('Enter quantity of people: '))

    # for item in cook_book:
    #     print(item[0].capitalize())
    #
    #     for k, v in item:
    #         pass
    #
    #     for line in item[1]:
    #         ingridient, quantity, num = line
    #         quantity = quantity * person
    #
    #         print(ingridient, quantity, num)
    #
    #     print('')