from less18 import validate_name, validate_age, advice
import unittest


class Testless18(unittest.TestCase):

    def setUp(self) -> None:
        self.name = validate_name
        self.age = validate_age
        self.advice = advice

    def test_validate_name_empty_string(self):
        self.assertEqual(self.name(''), 'Ошибка! Пожалуйста, введите Ваше имя!')

    def test_validate_name_shortname(self):
        self.assertEqual(self.name('Ян'), 'Ваше имя слишком короткое!')

    def test_validate_name_numbers(self):
        self.assertEqual(self.name('123'), 'Имя должно состоять из букв!')

    def test_validate_name_spaces(self):
        self.assertEqual(self.name('Ян де Витт'), 'Ошибка! Много пробелов в имени!')

    def test_validate_name_positive(self):
        self.assertEqual(self.name('Вася'), None)

    def test_validate_age_empty_string(self):
        self.assertEqual(self.age(''), 'Ошибка! Пожалуйста, введите Ваш возраст!')

    def test_validate_age_abc(self):
        self.assertIsNot(self.age('123'), 'Ошибка! Возраст должен состоять из цифр!')

    def test_validate_age_zero_year(self):
        self.assertEqual(self.age('0'), 'Вам не может быть 0 лет!')

    def test_validate_age_negative_num(self):
        self.assertEqual(self.age('-10'), 'Пожалуйста, введите корректное число!')

    def test_validate_age_less_than_14(self):
        self.assertEqual(self.age('10'), 'Вы не достигли нужного возраста!')

    def test_validate_age_positive(self):
        self.assertEqual(self.age('22'), None)

    def test_advice_16_years(self):
        self.assertEqual(self.advice(16), 'Вам необходимо получить паспорт!')

    def test_advice_17_years(self):
        self.assertEqual(self.advice(17), 'Вам необходимо получить паспорт!')

    def test_advice_25_years(self):
        self.assertEqual(self.advice(25), 'Вам необходимо заменить паспорт!')

    def test_advice_26_years(self):
        self.assertEqual(self.advice(26), 'Вам необходимо заменить паспорт!')

    def test_advice_45_years(self):
        self.assertEqual(self.advice(45), 'Вам необходимо заменить паспорт повторно!')

    def test_advice_46_years(self):
        self.assertEqual(self.advice(46), 'Вам необходимо заменить паспорт повторно!')

    def test_advice_more_than_47_years(self):
        self.assertEqual(self.advice(50), None)
