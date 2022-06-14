from less18 import validate_name, validate_age, advice
import unittest


class Testless18(unittest.TestCase):

    def setUp(self) -> None:
        self.name = validate_name
        self.age = validate_age
        self.advice = advice

    def test_validate_name(self):
        self.assertEqual(self.name(''), 'Ошибка! Пожалуйста, введите Ваше имя!')
        self.assertEqual(self.name('Ян'), 'Ваше имя слишком короткое!')
        self.assertEqual(self.name('123'), 'Имя должно состоять из букв!')
        self.assertEqual(self.name('Ян де Витт'), 'Ошибка! Много пробелов в имени!')
        self.assertEqual(self.name('Вася'), None)

    def test_validate_age(self):
        self.assertEqual(self.age(''), 'Ошибка! Пожалуйста, введите Ваш возраст!')
        self.assertIsNot(self.age('123'), 'Ошибка! Возраст должен состоять из цифр!')
        self.assertEqual(self.age('0'), 'Вам не может быть 0 лет!')
        self.assertEqual(self.age('-10'), 'Пожалуйста, введите корректное число!')
        self.assertEqual(self.age('10'), 'Вы не достигли нужного возраста!')
        self.assertEqual(self.age('22'), None)

    def test_advice(self):
        self.assertEqual(self.advice(16), 'Вам необходимо получить паспорт!')
        self.assertEqual(self.advice(17), 'Вам необходимо получить паспорт!')
        self.assertEqual(self.advice(25), 'Вам необходимо заменить паспорт!')
        self.assertEqual(self.advice(26), 'Вам необходимо заменить паспорт!')
        self.assertEqual(self.advice(45), 'Вам необходимо заменить паспорт повторно!')
        self.assertEqual(self.advice(46), 'Вам необходимо заменить паспорт повторно!')
        self.assertEqual(self.advice(50), None)

