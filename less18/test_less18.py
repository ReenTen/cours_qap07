import
import unittest

class Testless6(unittest.TestCase):

    def setUp(self):
        pass

    def test_validate_name(self):
        self.assertEqual(self.name(''), 'Ошибка! Пожалуйста, введите Ваше имя!')


if __name__ == '__main__':
    unittest.main()