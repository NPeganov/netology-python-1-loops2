import unittest
from task4 import max_amount_of_sales


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


if __name__ == '__main__':
    unittest.main()
