import unittest
from task5 import create_a_dict


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
