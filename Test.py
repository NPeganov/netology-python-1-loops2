import unittest
from task1 import unic_geo_tags

class test1(unittest.TestCase):
    def test_something(self):
        self.assertEqual({98, 35, 15, 213, 54, 119}, unic_geo_tags(
            {'user1': [213, 213, 213, 15, 213],
              'user2': [54, 54, 119, 119, 119],
              'user3': [213, 98, 98, 35]}))


if __name__ == '__main__':
    unittest.main()
