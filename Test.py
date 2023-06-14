import unittest
from task2 import quantity_of_words, percent_culc


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
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST5, percent_culc(self.INPUT_TASK2_TEST5_TOTAL,
                                                                        self.INPUT_TASK2_TEST5_NUM))

    def test6_for_percent_func(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST6, percent_culc(self.INPUT_TASK2_TEST6_TOTAL,
                                                                        self.INPUT_TASK2_TEST6_NUM))

    def test7_for_percent_func(self):
        self.assertEqual(self.EXPECTED_RESULT_TASK2_TEST7, percent_culc(self.INPUT_TASK2_TEST7_TOTAL,
                                                                        self.INPUT_TASK2_TEST7_NUM))


if __name__ == '__main__':
    unittest.main()
