import unittest

from task2 import quantity_of_words, percent_calc
from task3 import format_roi_output, ROI_add, ROI_calc, ROI_KEY, REVENUE, COST
from task5 import create_a_dict


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


if __name__ == '__main__':
    unittest.main()
