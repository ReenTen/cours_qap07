import datetime
import pytest
from less19 import validate_name, validate_age, advice


class Testless19:

    @pytest.fixture
    def setup(self) -> None:
        print(f'\n Начало запуска теста : {datetime.datetime.now()}')
        yield
        print(f'\n Конец теста : {datetime.datetime.now()}')
        print('--------------------------------------------------')

    @pytest.mark.parametrize(
        "name, message",
        [
            ('', 'Ошибка! Пожалуйста, введите Ваше имя!'),
            ('Ян', 'Ваше имя слишком короткое!'),
            ('123', 'Имя должно состоять из букв!'),
            ('Ян де Витт', 'Ошибка! Много пробелов в имени!'),
            ('Вася', None)
        ]
    )
    def test_validate_name(self, setup, name, message):
        assert validate_name(name) == message

    @pytest.mark.parametrize(
        "age, message",
        [
            ('', 'Ошибка! Пожалуйста, введите Ваш возраст!'),
            ('0', 'Вам не может быть 0 лет!'),
            ('-10', 'Пожалуйста, введите корректное число!'),
            ('10', 'Вы не достигли нужного возраста!'),
            ('22', None),

        ]
    )
    def test_validate_age(self, setup, age, message):
        assert validate_age(age) == message

    @pytest.mark.xfail
    @pytest.mark.parametrize(
        "age, message",
        [
            ('abcdef', 'Ошибка! Возраст должен состоять из цифр!'),
        ]
    )
    def test_validate_age_notequal(self, age, message):
        assert validate_age(age) == message

    @pytest.mark.parametrize(
        "age, message",
        [
            (16, 'Вам необходимо получить паспорт!'),
            (17, 'Вам необходимо получить паспорт!'),
            (25, 'Вам необходимо заменить паспорт!'),
            (26, 'Вам необходимо заменить паспорт!'),
            (45, 'Вам необходимо заменить паспорт повторно!'),
            (46, 'Вам необходимо заменить паспорт повторно!'),
            (50, None)
        ]
    )
    def test_advice(self, setup, age, message):
        assert advice(age) == message
