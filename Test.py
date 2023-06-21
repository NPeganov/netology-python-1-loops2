import unittest
from task6 import uniting, increasing, output


class TestForTask6(unittest.TestCase):
    EXPECTED_RESULT_TASK2_TEST1 = {
                                   ('сыр', 'гр'): 70,
                                   ('томаты', 'шт'): 2,
                                   ('огурцы', 'гр'): 20,
                                   ('маслины', 'гр'): 10,
                                   ('оливковое масло', 'мл'): 20,
                                   ('салат', 'гр'): 10,
                                   ('перец', 'гр'): 20,
                                   ('колбаса', 'гр'): 30,
                                   ('бекон', 'гр'): 30,
                                   ('оливки', 'гр'): 10,
                                   ('томаты', 'гр'): 20,
                                   ('тесто', 'гр'): 100,
                                   ('лимон', 'шт'): 1,
                                   ('вода', 'мл'): 200,
                                   ('сахар', 'гр'): 10,
                                   ('лайм', 'гр'): 20
                                   }
    INPUT_TASK2_TEST1 = {
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
    EXPECTED_RESULT_TASK2_TEST2 = {
                                   ('сыр', 'гр'): 160,
                                   ('томаты', 'шт'): 2,
                                   ('огурцы', 'гр'): 20,
                                   ('маслины', 'гр'): 20,
                                   ('оливковое масло', 'мл'): 20,
                                   ('салат', 'гр'): 10,
                                   ('перец', 'гр'): 50,
                                   ('колбаса', 'гр'): 30,
                                   ('бекон', 'гр'): 30,
                                   ('томаты', 'гр'): 20,
                                   ('тесто', 'гр'): 100,
                                   ('лимон', 'шт'): 1,
                                   ('вода', 'мл'): 200,
                                   ('сахар', 'гр'): 10,
                                   ('мята', 'гр'): 30
                                   }
    INPUT_TASK2_TEST2 = {
        'салат': [
            {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
            {'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
            {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
            {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
            {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
            {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
            {'ingridient_name': 'перец', 'quantity': 50, 'measure': 'гр'}
        ],
        'пицца': [
            {'ingridient_name': 'сыр', 'quantity': 110, 'measure': 'гр'},
            {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
            {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
            {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
            {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
            {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
        ],
        'лимонад': [
            {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
            {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
            {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
            {'ingridient_name': 'мята', 'quantity': 30, 'measure': 'гр'},
        ]
    }

    EXPECTED_RESULT_TASK2_TEST3 = {
                                   ('сыр', 'гр'): 70,
                                   ('томаты', 'шт'): 2,
                                   ('огурцы', 'гр'): 20,
                                   ('маслины', 'гр'): 10,
                                   ('оливковое масло', 'мл'): 20,
                                   ('салат', 'гр'): 10,
                                   ('перец', 'гр'): 20,
                                   ('колбаса', 'гр'): 30,
                                   ('бекон', 'гр'): 30,
                                   ('оливки', 'гр'): 10,
                                   ('томаты', 'гр'): 20,
                                   ('тесто', 'гр'): 100,
                                   ('лимон', 'шт'): 1,
                                   ('вода', 'мл'): 200,
                                   ('сахар', 'гр'): 10,
                                   ('лайм', 'гр'): 20
                                   }

    INPUT_TASK2_TEST3_MULTIPLIER = 1
    INPUT_TASK2_TEST3_RESULT_DICT = {
                                   ('сыр', 'гр'): 70,
                                   ('томаты', 'шт'): 2,
                                   ('огурцы', 'гр'): 20,
                                   ('маслины', 'гр'): 10,
                                   ('оливковое масло', 'мл'): 20,
                                   ('салат', 'гр'): 10,
                                   ('перец', 'гр'): 20,
                                   ('колбаса', 'гр'): 30,
                                   ('бекон', 'гр'): 30,
                                   ('оливки', 'гр'): 10,
                                   ('томаты', 'гр'): 20,
                                   ('тесто', 'гр'): 100,
                                   ('лимон', 'шт'): 1,
                                   ('вода', 'мл'): 200,
                                   ('сахар', 'гр'): 10,
                                   ('лайм', 'гр'): 20
                                   }

    EXPECTED_RESULT_TASK2_TEST4 = {
                                   ('сыр', 'гр'): 320,
                                   ('томаты', 'шт'): 4,
                                   ('огурцы', 'гр'): 40,
                                   ('маслины', 'гр'): 40,
                                   ('оливковое масло', 'мл'): 40,
                                   ('салат', 'гр'): 20,
                                   ('перец', 'гр'): 100,
                                   ('колбаса', 'гр'): 60,
                                   ('бекон', 'гр'): 60,
                                   ('томаты', 'гр'): 40,
                                   ('тесто', 'гр'): 200,
                                   ('лимон', 'шт'): 2,
                                   ('вода', 'мл'): 400,
                                   ('сахар', 'гр'): 20,
                                   ('мята', 'гр'): 60
                                   }

    INPUT_TASK2_TEST4_MULTIPLIER = 2
    INPUT_TASK2_TEST4_RESULT_DICT = {
                                   ('сыр', 'гр'): 160,
                                   ('томаты', 'шт'): 2,
                                   ('огурцы', 'гр'): 20,
                                   ('маслины', 'гр'): 20,
                                   ('оливковое масло', 'мл'): 20,
                                   ('салат', 'гр'): 10,
                                   ('перец', 'гр'): 50,
                                   ('колбаса', 'гр'): 30,
                                   ('бекон', 'гр'): 30,
                                   ('томаты', 'гр'): 20,
                                   ('тесто', 'гр'): 100,
                                   ('лимон', 'шт'): 1,
                                   ('вода', 'мл'): 200,
                                   ('сахар', 'гр'): 10,
                                   ('мята', 'гр'): 30
                                   }

    EXPECTED_RESULT_TASK2_TEST5 = """Сыр: 210 гр 
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
    INPUT_TASK2_TEST5 = {
                         ('сыр', 'гр'): 210,
                         ('томаты', 'шт'): 6,
                         ('огурцы', 'гр'): 60,
                         ('маслины', 'гр'): 30,
                         ('оливковое масло', 'мл'): 60,
                         ('салат', 'гр'): 30,
                         ('перец', 'гр'): 60,
                         ('колбаса', 'гр'): 90,
                         ('бекон', 'гр'): 90,
                         ('оливки', 'гр'): 30,
                         ('томаты', 'гр'): 60,
                         ('тесто', 'гр'): 300,
                         ('лимон', 'шт'): 3,
                         ('вода', 'мл'): 600,
                         ('сахар', 'гр'): 30,
                         ('лайм', 'гр'): 60
                         }

    EXPECTED_RESULT_TASK2_TEST6 = """Сыр: 70 гр 
Томаты: 2 шт 
Огурцы: 20 гр 
Маслины: 10 гр 
Оливковое масло: 20 мл 
Салат: 10 гр 
Перец: 20 гр 
Колбаса: 30 гр 
Бекон: 30 гр 
Оливки: 10 гр 
Томаты: 20 гр 
Тесто: 100 гр 
Лимон: 1 шт 
Вода: 200 мл 
Сахар: 10 гр 
Лайм: 20 гр 
"""
    INPUT_TASK2_TEST6 = {
                         ('сыр', 'гр'): 70,
                         ('томаты', 'шт'): 2,
                         ('огурцы', 'гр'): 20,
                         ('маслины', 'гр'): 10,
                         ('оливковое масло', 'мл'): 20,
                         ('салат', 'гр'): 10,
                         ('перец', 'гр'): 20,
                         ('колбаса', 'гр'): 30,
                         ('бекон', 'гр'): 30,
                         ('оливки', 'гр'): 10,
                         ('томаты', 'гр'): 20,
                         ('тесто', 'гр'): 100,
                         ('лимон', 'шт'): 1,
                         ('вода', 'мл'): 200,
                         ('сахар', 'гр'): 10,
                         ('лайм', 'гр'): 20
                         }

    EXPECTED_RESULT_TASK2_TEST7 = """Сыр: 350 гр 
Томаты: 10 шт 
Огурцы: 100 гр 
Маслины: 50 гр 
Оливковое масло: 100 мл 
Салат: 50 гр 
Перец: 100 гр 
Колбаса: 150 гр 
Бекон: 150 гр 
Оливки: 50 гр 
Томаты: 100 гр 
Тесто: 500 гр 
Лимон: 5 шт 
Вода: 1000 мл 
Сахар: 50 гр 
Лайм: 100 гр 
"""
    INPUT_TASK2_TEST7 = {
                         ('сыр', 'гр'): 350,
                         ('томаты', 'шт'): 10,
                         ('огурцы', 'гр'): 100,
                         ('маслины', 'гр'): 50,
                         ('оливковое масло', 'мл'): 100,
                         ('салат', 'гр'): 50,
                         ('перец', 'гр'): 100,
                         ('колбаса', 'гр'): 150,
                         ('бекон', 'гр'): 150,
                         ('оливки', 'гр'): 50,
                         ('томаты', 'гр'): 100,
                         ('тесто', 'гр'): 500,
                         ('лимон', 'шт'): 5,
                         ('вода', 'мл'): 1000,
                         ('сахар', 'гр'): 50,
                         ('лайм', 'гр'): 100
                         }

    def test1_for_forming_new_dict(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST1, uniting(self.INPUT_TASK2_TEST1))

    def test2_for_forming_new_dict(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST2, uniting(self.INPUT_TASK2_TEST2))

    def test3_for_multiplying(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST3, increasing(self.INPUT_TASK2_TEST3_MULTIPLIER,
                                                                      self.INPUT_TASK2_TEST3_RESULT_DICT))

    def test4_for_multiplying(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST4, increasing(self.INPUT_TASK2_TEST4_MULTIPLIER,
                                                                      self.INPUT_TASK2_TEST4_RESULT_DICT))

    def test5_for_output(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST5, output(self.INPUT_TASK2_TEST5))

    def test6_for_output(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST6, output(self.INPUT_TASK2_TEST6))

    def test7_for_output(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST7, output(self.INPUT_TASK2_TEST7))


if __name__ == '__main__':
    unittest.main()
