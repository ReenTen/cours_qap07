from typing import Optional  # Добавление модуля тайпинга.


def validate_name(name: str) -> Optional[str]:
    """
Функция проверки имени.
Если вводимое имя не соответствует критериям,
Выводится ошибка по одному из критериев
Если имя введено верно - ничего не выводим (или None).
    """
    if not name:  # Проверяем сразу на пустую строку, иначе конфликт со 2 проверкой.
        return 'Ошибка! Пожалуйста, введите Ваше имя!'
    elif len(name) < 3:  # Если длина имени меньше 3 символов.
        return 'Ваше имя слишком короткое!'
    elif name.isdigit():  # Если имя состоит из цифр
        return 'Имя должно состоять из букв!'
    if name.count(' ') > 1:  # Если количество пробелов в имени больше 1.
        return 'Ошибка! Много пробелов в имени!'

    return  # Если имя верное - ничего не выводим.


def advice(age: int):
    """
Функция проверки возраста с советом по замене паспорта.
Если вводимый возраст не соответствует критериям,
Ничего не выводим (или None).
Если возраст соответствует критериям - выводим совет.
    """
    if int(age) in range(16, 18):  # Если возраст равен 16 или 17.
        return 'Вам необходимо получить паспорт!'
    elif int(age) in range(25, 27):  # Если возраст равен 25 или 26.
        return 'Вам необходимо заменить паспорт!'
    elif int(age) in range(45, 47):  # Если возраст равен 45 или 46.
        return 'Вам необходимо заменить паспорт повторно!'

    return  # Если возраст не соответствует критекиям - ничего не выводим.


def validate_age(age: str) -> Optional[str]:
    """
Функция проверки возраста.
Если вводимый возраст не соответствует критериям,
Выводится ошибка по одному из критериев
Если возраст введен верно - переходим к функции advice.
    """
    if not age:  # Если пустая строка.
        return 'Ошибка! Пожалуйста, введите Ваш возраст!'
    elif not age.isdigit:  # Если возраст не из цифр (not age.isdigit учитывает спецсимволы).
        return 'Ошибка! Возраст должен состоять из цифр!'
    elif int(age) == 0:  # Если возраст равен 0.
        return 'Вам не может быть 0 лет!'
    elif int(age) < 0:  # Если возраст меньше 0.
        return 'Пожалуйста, введите корректное число!'
    elif 0 < int(age) < 14:  # Если возраст от 0 до 14 лет (не включая 14)
        return 'Вы не достигли нужного возраста!'

    return advice(age)  # Если возраст соответствует критериям, переходим к функции совета.


# def main():
#     """
# Функция вызова.
# Создаём цикл проверки данных.
# Вводим данные (имя и возраст).
# Присваеваем переменной error_message ошибки при  проверке имени/возраста.
# Пока данные вводятся с ошибкой (input(name) и input(age) == true)
# Выводим сообщение с ошибкой (error_messsage) и переходим в начало цикла.
# Если данные введены без ошибок (input(name) и input(age) == false)
# Пропускаем (прерываем) цикл проверки.
#     """
#     while True:  # Бескончный цикл проверки, пока условие не будет == False.
#         name = input('Введите Ваше имя: ').capitalize().strip()  # Вводим имя
#         age = input(f'Введите Ваш возраст: ')  # Вводим возраст
#         error_message = (validate_name(name) or '') + (validate_age(age) or '')
#         # validate_name(name) может вернуть строку или None.
#         # При конкатенации складываются одинаковые типы данных.
#         # Поэтому в условие добавляем or '' (пустая строка - none).
#         if not error_message:  # Если данные введены верно
#             break  # Прерываем цикл
#         print(error_message)  # Если не верно - выводим сообщение об ошибке. Переходим к началу цикла.
#         break  # Выход из цикла при полной проверке имени/возраста/совета.
#
#
# main()
