import unittest
from task1 import unic_geo_tags


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


if __name__ == '__main__':
    unittest.main()
