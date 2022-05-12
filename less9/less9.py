# 1. Написать лямбда-функцию, определяющую чёт/нечет.
# Функция принимает парамерт и выдаёт слово (чёт\нечет).
# 2. Дан список чисел. Вернуть список, где при помощи ф-ции map() каждое число переведео в строку.
# В кач-ве ф-ции в map() исп лямбду.
# 3. При помощи filter отфильтровать те слова из кортежа, которые являются полиндромами.
# 4. Написать декоратор к 2 любым ф-циям, который бы считал и выводил время их выполнения.
# 5. ** ( И тут я сдался, ибо не хватило сил :( )

from datetime import datetime
from time import time, sleep
from math import sqrt, sin, tan

num1 = [2, 11, 32, 117, 98]
print(
    list(
        map(
            lambda x: 'Чётное' if x % 2 == 0 else 'Не очень чётное', num1
        )
    )
)

print()

num2 = [13, 44, 279, 9, 63]
print(
    list(
        map(
            lambda x: str(x), num2
        )
    )
)

print()

cort = ['мама', 'казак', 'корт', 'поп', 'довод', 'карта']
print(
    list(
        filter(
            lambda x: x == x[::-1], cort
        )
    )
)

print()


def decorator(func):
    def wrapper():
        curr_time = datetime.now()
        start_time = time()
        print(f'Начало выполнения функции {func.__name__} - {curr_time}')
        result = func()
        curr_time = datetime.now()
        end_time = time()
        total_time = end_time - start_time
        print(f'Конец выполнения функции {func.__name__} - {curr_time}')
        print(f'Время выполнения функции {func.__name__} - {total_time}')
        return result

    return wrapper


@decorator
def math():
    sleep(1)
    print(round(sin(144), 1),
          round(tan(217), 2),
          round(sqrt((299 ** 7)), 1)
          )


math()

print()


@decorator
def coub():
    sleep(2)
    print(79794679 ** 3,
          874873658 ** 3,
          -573835683 ** 3,
          )


coub()
