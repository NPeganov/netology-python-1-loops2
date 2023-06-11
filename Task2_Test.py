import unittest
from task2 import quantity_of_words


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual({3: 4, 2: 3}, quantity_of_words([
            'смотреть сериалы онлайн',
            'новости спорта',
            'афиша кино',
            'курс доллара',
            'сериалы этим летом',
            'курс по питону',
            'сериалы про спорт',
        ]))


if __name__ == '__main__':
    unittest.main()
