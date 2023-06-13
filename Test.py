import unittest
from task3 import format_roi_output, ROI_add, ROI_calc, ROI_KEY


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
        test_dict = {'foo': {'revenue': self.TEST_REVENUE, 'cost': self.TEST_COST_POSITIVE}}
        ROI_add(test_dict)
        self.assertTrue(ROI_KEY in test_dict.get('foo'))

    def test_roi_calc_positive(self):
        self.assertEqual(self.EXPECTED_ROI_POSITIVE, ROI_calc(self.TEST_REVENUE, self.TEST_COST_POSITIVE))

    def test_roi_calc_negative(self):
        self.assertEqual(self.EXPECTED_ROI_NEGATIVE, ROI_calc(self.TEST_REVENUE, self.TEST_COST_NEGATIVE))


if __name__ == '__main__':
    unittest.main()
