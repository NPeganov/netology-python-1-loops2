import unittest
from task1 import unic_geo_tags
from task2 import quantity_of_words, percent_calc
from task3 import format_roi_output, ROI_add, ROI_calc, ROI_KEY, REVENUE, COST
from task4 import max_amount_of_sales
from task5 import create_a_dict
from task6 import uniqify_ingridients, qnty_calc, output


class TestForTask1(unittest.TestCase):
    EXPECTED_RESULT_TASK1_TEST1 = {98, 35, 15, 213, 54, 119}
    INPUT_TASK1_TEST1 = {'user1': [213, 213, 213, 15, 213],
                         'user2': [54, 54, 119, 119, 119],
                         'user3': [213, 98, 98, 35]}

    EXPECTED_RESULT_TASK1_TEST2 = {98, 35, 548, 199, 45, 15, 18, 213, 54, 119}
    INPUT_TASK1_TEST2 = {'user1': [45, 213, 54, 15, 213],
                         'user2': [54, 54, 548, 119, 199],
                         'user3': [213, 18, 98, 35]}

    EXPECTED_RESULT_TASK1_TEST3 = {96, 613, 518, 197, 27, 38, 458, 16, 913, 18, 19, 84, 56, 283}
    INPUT_TASK1_TEST3 = {'user1': [56, 613, 96, 16, 283],
                         'user2': [84, 27, 518, 19, 197],
                         'user3': [913, 18, 458, 38]}

    def test1(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK1_TEST1, unic_geo_tags(self.INPUT_TASK1_TEST1))

    def test2(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK1_TEST2, unic_geo_tags(self.INPUT_TASK1_TEST2))

    def test3(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK1_TEST3, unic_geo_tags(self.INPUT_TASK1_TEST3))


class TestFotTask2(unittest.TestCase):
    EXPECTED_RESULT_TASK2_TEST1 = {3: 4, 2: 3}
    INPUT_TASK2_TEST1 = [
            'смотреть сериалы онлайн',
            'новости спорта',
            'афиша кино',
            'курс доллара',
            'сериалы этим летом',
            'курс по питону',
            'сериалы про спорт'
        ]

    EXPECTED_RESULT_TASK2_TEST2 = {3: 4, 1: 2, 7: 1}
    INPUT_TASK2_TEST2 = [
            'реферат по биологии',
            'поступление в МГУ',
            'github',
            'проект или проэкт',
            'очень странные дела 5 сезон дата выхода',
            'рецепты с курицей',
            'мстители'
        ]

    EXPECTED_RESULT_TASK2_TEST3 = {5: 3, 3: 2, 6: 1, 2: 1}
    INPUT_TASK2_TEST3 = [
            'есть ли жизнь на Марсе',
            'расстояние он Земли до Сатурна',
            'гороскоп на июль',
            'в каком году был основан Google',
            'площадь Аргентины',
            'когда пасха в этом году',
            'квартиры в Москве'
        ]

    EXPECTED_RESULT_TASK2_TEST4 = {4: 1, 3: 2}
    INPUT_TASK2_TEST4 = [
            'Алиса в стране чудес',
            'льняное масло купить',
            'Александр Пушкин детство'
        ]

    EXPECTED_RESULT_TASK2_TEST5 = 42.857142857142854
    INPUT_TASK2_TEST5_NUM = 3
    INPUT_TASK2_TEST5_TOTAL = 7

    EXPECTED_RESULT_TASK2_TEST6 = 57.142857142857146
    INPUT_TASK2_TEST6_NUM = 4
    INPUT_TASK2_TEST6_TOTAL = 7

    EXPECTED_RESULT_TASK2_TEST7 = 33.333333333333336
    INPUT_TASK2_TEST7_NUM = 1
    INPUT_TASK2_TEST7_TOTAL = 3

    def test1(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST1, quantity_of_words(self.INPUT_TASK2_TEST1))

    def test2(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST2, quantity_of_words(self.INPUT_TASK2_TEST2))

    def test3(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST3, quantity_of_words(self.INPUT_TASK2_TEST3))

    def test4(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST4, quantity_of_words(self.INPUT_TASK2_TEST4))

    def test5_for_percent_func(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST5, percent_calc(self.INPUT_TASK2_TEST5_TOTAL,
                                                                        self.INPUT_TASK2_TEST5_NUM))

    def test6_for_percent_func(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST6, percent_calc(self.INPUT_TASK2_TEST6_TOTAL,
                                                                        self.INPUT_TASK2_TEST6_NUM))

    def test7_for_percent_func(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST7, percent_calc(self.INPUT_TASK2_TEST7_TOTAL,
                                                                        self.INPUT_TASK2_TEST7_NUM))

        
class TestForTask3(unittest.TestCase):
    EXPECTED_RESULT_TASK3_TEST1 = """{'adwords': {'revenue': 35, 'cost': 34, 'ROI': 2.94},
 'facebook': {'revenue': 103, 'cost': 110, 'ROI': -6.36},
 'twitter': {'revenue': 11, 'cost': 24, 'ROI': -54.17},
 'vk': {'revenue': 103, 'cost': 98, 'ROI': 5.1},
 'yandex': {'revenue': 179, 'cost': 153, 'ROI': 16.99}}"""

    INPUT_TASK3_TEST1 = {
        'vk': {'revenue': 103, 'cost': 98},
        'yandex': {'revenue': 179, 'cost': 153},
        'facebook': {'revenue': 103, 'cost': 110},
        'adwords': {'revenue': 35, 'cost': 34},
        'twitter': {'revenue': 11, 'cost': 24},
    }

    TEST_REVENUE = 6
    TEST_COST_POSITIVE = 2
    EXPECTED_ROI_POSITIVE = 200
    TEST_COST_NEGATIVE = 0
    EXPECTED_ROI_NEGATIVE = 0

    def test_output_format(self):
        self.assertEqual(format_roi_output(self.INPUT_TASK3_TEST1), self.EXPECTED_RESULT_TASK3_TEST1)

    def test_roi_addon(self):
        test_dict = {'foo': {REVENUE: self.TEST_REVENUE, COST: self.TEST_COST_POSITIVE}}
        ROI_add(test_dict)
        self.assertTrue(ROI_KEY in test_dict.get('foo'))

    def test_roi_calc_positive(self):
        self.assertEqual(self.EXPECTED_ROI_POSITIVE, ROI_calc(self.TEST_REVENUE, self.TEST_COST_POSITIVE))

    def test_roi_calc_negative(self):
        self.assertEqual(self.EXPECTED_ROI_NEGATIVE, ROI_calc(self.TEST_REVENUE, self.TEST_COST_NEGATIVE))
        
        
class TestForTask4(unittest.TestCase):
    EXPECTED_RESULT_TASK4_TEST1 = 'vk'
    INPUT_TASK4_TEST1 = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

    EXPECTED_RESULT_TASK4_TEST2 = 'ok'
    INPUT_TASK4_TEST2 = {'facebook': 550, 'yandex': 118, 'vk': 10, 'google': 94, 'email': 427, 'ok': 958}

    EXPECTED_RESULT_TASK4_TEST3 = 'vk'
    INPUT_TASK4_TEST3 = {'facebook': 50, 'yandex': 18, 'vk': 140, 'google': 64, 'email': 27, 'ok': 58}

    def test1(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK4_TEST1, max_amount_of_sales(self.INPUT_TASK4_TEST1))

    def test2(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK4_TEST2, max_amount_of_sales(self.INPUT_TASK4_TEST2))

    def test3(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK4_TEST3, max_amount_of_sales(self.INPUT_TASK4_TEST3))
        

class TestForTask5(unittest.TestCase):
    EXPECTED_RESULT_TASK5_TEST1 = {'2018-01-01': {'yandex': {'cpc': 100}}}
    INPUT_TASK5_TEST1 = ['2018-01-01', 'yandex', 'cpc', 100]

    EXPECTED_RESULT_TASK5_TEST2 = {'a': {'b': {'c': {'d': {'e': 'f'}}}}}
    INPUT_TASK5_TEST2 = ['a', 'b', 'c', 'd', 'e', 'f']

    EXPECTED_RESULT_TASK5_TEST3 = {'linux': {'ubuntu': {'fedora': 'windows'}}}
    INPUT_TASK5_TEST3 = ['linux', 'ubuntu', 'fedora', 'windows']

    def test1(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK5_TEST1, create_a_dict(self.INPUT_TASK5_TEST1))

    def test2(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK5_TEST2, create_a_dict(self.INPUT_TASK5_TEST2))

    def test3(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK5_TEST3, create_a_dict(self.INPUT_TASK5_TEST3))

        
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
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST1, uniqify_ingridients(self.INPUT_TASK2_TEST1))

    def test2_for_forming_new_dict(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST2, uniqify_ingridients(self.INPUT_TASK2_TEST2))

    def test3_for_multiplying(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST3, qnty_calc(self.INPUT_TASK2_TEST3_MULTIPLIER,
                                                                     self.INPUT_TASK2_TEST3_RESULT_DICT))

    def test4_for_multiplying(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST4, qnty_calc(self.INPUT_TASK2_TEST4_MULTIPLIER,
                                                                     self.INPUT_TASK2_TEST4_RESULT_DICT))

    def test5_for_output(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST5, output(self.INPUT_TASK2_TEST5))

    def test6_for_output(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST6, output(self.INPUT_TASK2_TEST6))

    def test7_for_output(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST7, output(self.INPUT_TASK2_TEST7))


if __name__ == '__main__':
    unittest.main()
