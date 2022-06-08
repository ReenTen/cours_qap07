# 1. Сохранить данные о машине в файл в json формате.
# 2. Доделать классы машин, сделав их датаклассом. Сделать возможность сравнения по году выпуска машин.
# 3. Загрузить машины из json файла.
# 4. Написать функцию, которая создает несколько машин и сохраняет их в файл, если файла нет или он пустой.

import dataclasses
import json
import os
from abc import ABC
from dataclasses import dataclass
from math import tan


@dataclass(order=True)
class Cars(ABC):
    label: str
    mod: str  # modifications (тип машины)
    capacity: int
    fuel_cap: int  # fuel_capacity (Объём топливного бака)
    fuel_cons: int  # fuel_consumption (расход топлива)
    max_speed: int
    color: str
    year: int
    _curr_speed: int = 0
    time: float = 0.0

    print('Запускаем производство автомобилей.\n')

    def info(self):
        print(
            f'Начинаем выпуск машин марки {self.label}.\n'
            f'Модификация - {self.mod}.\n'
            f'Мощность - {self.capacity} л.с.\n'
            f'Объем топливного бака - {self.fuel_cap} литров.\n'
            f'Расход топлива - {self.fuel_cons}, л/100 км.\n'
            f'Максимальная скорость равна {self.max_speed} км/ч.\n'
            f'Цвет машины - {self.color}.\n'
            f'Год выпуска - {self.year}.\n'

        )

    def distance(self):
        self.time = 1000 / self.max_speed
        print(f'На максимальной скорости'
              f'машина проедет расстояние в 1000 км за {self.time.__round__(1)} часа.')


@dataclass(order=True)
class BMW(Cars):
    label: str = 'BMW'
    mod: str = 'xDrive 35i'
    capacity: int = 306
    fuel_cap: int = 85
    fuel_cons: float = 10.1
    max_speed: int = 235
    color: str = 'красный'
    year: int = 2008

    def car_speed(self, add_speed: int):
        self._curr_speed = self._curr_speed + add_speed
        if self._curr_speed < self.max_speed:
            print(f'Текущая скорость машины равна {self._curr_speed} км/ч.')
        if self._curr_speed == self.max_speed:
            print(f'Вы достигли максимальной скорости {self._curr_speed} км/ч.')
        if self._curr_speed > self.max_speed:
            print(f'Машина не может ехать быстрее максимальной скорости! '
                  f'Макcимальная скорость {self.max_speed} км/ч.'
                  )


@dataclass(order=True)
class Audi(Cars):
    label: str = 'Audi'
    mod: str = '4.0 TFSI Quattro'
    capacity: int = 519
    fuel_cap: int = 82
    fuel_cons: float = 10.2
    max_speed: int = 250
    color: str = 'белый'
    year: int = 2009


@dataclass(order=True)
class Kia(Cars):
    label: str = 'Kia'
    mod: str = 'K9'
    capacity: int = 300
    fuel_cap: int = 77
    fuel_cons: float = 9.8
    max_speed: int = 260
    color: str = 'синий'
    year: int = 2010

    @staticmethod
    def braking_dist_max(max_speed):
        print(f'Тормозной пусть при максимальной скорости составляет '
              f'{(max_speed / 10) * (max_speed / 10)} метров')

    @staticmethod
    def turning_angle(wheels_base, turn_angle):
        print(f'Радиус разворота машины составляет {round(wheels_base / tan(turn_angle), 2)} метров.')

    @classmethod
    def only_pink_car(cls):
        car_kia = cls(color='розовый')
        car_kia.info()

    @property
    def max_speed_mph(self):
        return self.max_speed * 1.5


def car_create():
    """
    Функиця, которая создает несколько машин и сохраняет их в файл,
    если файла нет или он пустой.
    """
    bmw_x6 = BMW(label='BMW_X6', mod='xDrive 50i', capacity=406, fuel_cap=85, fuel_cons=12.5, max_speed=250,
                 color='black', year=2009)
    audi_sq5 = Audi('Audi_SQ5', '3.0 TFSI', 354, 63, 8.5, 250, 'white', 2012)
    kia_bor = Kia('Kia_borrego', '4,6 V8 DOHC', 337, 78, 13.4, 230, 'grey', 2010)

    new_car_list = [    # Создаём кортеж из dict для записи данных о новых машинах в json.
        {
            'label': bmw_x6.label,
            'mod': bmw_x6.mod,
            'capacity': bmw_x6.capacity,
            'fuel_cap': bmw_x6.fuel_cap,
            'fuel_cons': bmw_x6.fuel_cons,
            'max_speed': bmw_x6.max_speed,
            'color': bmw_x6.color,
            'year': bmw_x6.year
        },
        {
            'label': audi_sq5.label,
            'mod': audi_sq5.mod,
            'capacity': audi_sq5.capacity,
            'fuel_cap': audi_sq5.fuel_cap,
            'fuel_cons': audi_sq5.fuel_cons,
            'max_speed': audi_sq5.max_speed,
            'color': audi_sq5.color,
            'year': audi_sq5.year
        },
        {
            'label': kia_bor.label,
            'mod': kia_bor.mod,
            'capacity': kia_bor.capacity,
            'fuel_cap': kia_bor.fuel_cap,
            'fuel_cons': kia_bor.fuel_cons,
            'max_speed': kia_bor.max_speed,
            'color': kia_bor.color,
            'year': kia_bor.year
        }
    ]

    def json_exist(file_name):
        """
        Функция, которая возвращает путь файла, если он открыт или существует в системе.
        """
        return os.path.exists(file_name)

    if json_exist('new_car_list.json'):  # Если new_car_list.json существует
        with open('new_car_list.json', 'w', encoding="utf-8") as f:  # Открываем файл на запись
            json.dump(new_car_list, f, indent=4, ensure_ascii=False)  # Записываем данные из dict new_car_list
    else:  # Если не существует
        with open('new_car_list.json', 'w', encoding="utf-8") as f:
            # Создаём и открываем на запись файл new_car_list.json
            json.dump(new_car_list, f, indent=4, ensure_ascii=False)  # Записываем данные из dict new_car_list


def main():
    car_bmw = BMW()
    car_bmw.info()
    car_bmw.distance()
    car_bmw.car_speed(300)
    print()
    car_audi = Audi()
    car_audi.info()
    car_audi.distance()
    print()
    car_kia = Kia()
    car_kia.info()
    car_kia.distance()
    print()

    Kia.braking_dist_max(350)
    print()
    Kia.turning_angle(3, 35)
    print()
    Kia.only_pink_car()

    print(car_kia.year == car_audi.year)  # Сравнение машин по году выпуска
    print()

    bmw = dataclasses.asdict(car_bmw)  # Создаём dict из атрибутов объекта класса car_bmw
    kia = dataclasses.asdict(car_kia)  # Создаём dict из атрибутов объекта класса car_kia
    audi = dataclasses.asdict(car_audi)  # Создаём dict из атрибутов объекта класса car_audi

    curr_cars = [bmw, kia, audi]  # Создаём кортеж из dict для записи данных о текущих машинах в json.

    with open('current_car_list.json', 'w', encoding="utf-8") as data:  # Открываем current_car_list.json на запись
        json.dump(curr_cars, data, indent=4, ensure_ascii=False)
        # Записываем данные из curr_cars, которая хранит данные о машинах, прописанных в датаклассах.

    with open('to_dataclass.json', encoding="utf-8") as json_file:
        # Подгрузка информации о новой машине из to_dataclass.json в датакласс.
        new_data = json.load(json_file)[0]    #

    new_bmw = BMW(**new_data)
    # ** - распаковка информации о новой машине из new_data в датакласс BMW.

    new_bmw.info()    # Вызываем метод info у объекта класса new_bmw с информацией, загруженной из json (проверка).

    car_create()


if __name__ == '__main__':
    main()
