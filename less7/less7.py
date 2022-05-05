# 1. Реализовать абстрактный класс машины
# (придумать методы, какие есть у машины, какие нужно переопределить
# у дочерних классов, какие будут с общей готовой реализацией).
# 2. Реализовать несколько классов разных марок машин, наследуемых от базового класса.
# Переопределить абстрактные методы, свойства, придумать новые методы, которые есть у конкретных машин.
# 3. Реализовать абстрактный класс самолета. Должно быть один/несколько одноименных атрибутов класса машины (п1).
# 4. Реализовать несколько классов разных марок самолёта (п2).
# 5. Созд. неск. экземпляров каждой машины\самолёта, вызвать разл. методы у объектов.
# 6. Сделать коллекцию из объектов и через цикл вызвать те объекты, которые есть в обоихх классах.

class Cars:  # Создаем родительский абстрактный класс "Машины"

    def __init__(self,
                 label: str = '',
                 mod: str = '',  # modifications (тип машины)
                 capacity: int = '',
                 fuel_cap: int = '',  # fuel_capacity (Объём топливного бака)
                 fuel_cons: int = '',  # fuel_consumption (расход топлива)
                 max_speed: int = '',
                 weight: int = 2,
                 color: str = 'черный',
                 doors: int = 4,
                 ):
        """
        Создаем конструктор класса.
        Конструктор вызывается автоматически при создании нового объекта класса
        с указанием базовых атрибутов, описанных в конструкторе.
        """
        self.label = label
        self.mod = mod
        self.capacity = capacity
        self.fuel_cap = fuel_cap
        self.fuel_cons = fuel_cons
        self.max_speed = max_speed
        self.weight = weight
        self.color = color
        self.doors = doors

        self._curr_speed = 0
        self.time = 0

        print('Запускаем производство автомобилей.\n')

    def info(self):
        """
        Создаём функцию, выводящую информацию об объектах класса.
        Т.к. функция находится в родительском классе,
        Она может быть вызвана в дочерних классах.
        """
        print(
            f'Начинаем выпуск машин марки {self.label}.\n'
            f'Модификация - {self.mod}.\n'
            f'Мощность - {self.capacity} л.с.\n'
            f'Объем топливного бака - {self.fuel_cap} литров.\n'
            f'Расход топлива - {self.fuel_cons}, л/100 км.\n'
            f'Максимальная скорость равна {self.max_speed} км/ч.\n'
            f'Вес авто - {self.weight} тонны.\n'
            f'Базовый окрас - {self.color}.\n'
            f'Колиичество дверей - {self.doors}.\n'

        )

    def distance(self):
        """
        Создаём функцию, определяющую время прохождения расстояния
        при максимальной скорости.
        Т.к. функция находится в родительском классе,
        Она может быть вызвана в дочерних классах.
        """
        self.time = 1000 / self.max_speed
        print(f'На максимальной скорости'
              f'машина проедет расстояние в 1000 км за {self.time.__round__(1)} часа.')
        # Округляем полученное значение


class BMW(Cars):  # Создаём дочерний класс BMW, который наследуется от родительского класса Машины.

    def __init__(self, label='BMW', mod='xDrive 35i', capacity=306, fuel_cap=85, fuel_cons=10.1, max_speed=235,
                 color='красный'):
        """
        Создаём функцию, которая переопределяет атрибуты родительского класса Машины.
        """
        super().__init__(label, mod, capacity, fuel_cap, fuel_cons, max_speed, color)
        # Обращаемся к родительскому классу.

    def car_speed(self, add_speed: int):
        """
        Создаём функцию, которая определяет текущую скорость машины класса BMW.
        Функция относится к дочернему классу BMW,
        поэтому может быть вызвана только для объектов данного класса.
        """
        self._curr_speed = self._curr_speed + add_speed
        if self._curr_speed < self.max_speed:
            print(f'Текущая скорость машины равна {self._curr_speed} км/ч.')
        if self._curr_speed == self.max_speed:
            print(f'Вы достигли максимальной скорости {self._curr_speed} км/ч.')
        if self._curr_speed > self.max_speed:
            print(f'Машина не может ехать быстрее максимальной скорости! '
                  f'Макcимальная скорость {self.max_speed} км/ч.'
                  )


class Audi(Cars):  # Создаём дочерний класс Audi, который наследуется от родительского класса Машины.

    def __init__(self, label='Audi', mod='4.0 TFSI Quattro', capacity=519, fuel_cap=82, fuel_cons=10.2, max_speed=250,
                 color='белый'):
        """
        Создаём функцию, которая переопределяет атрибуты родительского класса Машины.
        """
        super().__init__(label, mod, capacity, fuel_cap, fuel_cons, max_speed, color)


class Kia(Cars):  # Создаём дочерний класс Kia, который наследуется от родительского класса Машины.
    def __init__(self, label='Kia', mod='K9', capacity=300, fuel_cap=77, fuel_cons=9.8, max_speed=260,
                 color='синий'):
        """
        Создаём функцию, которая переопределяет атрибуты родительского класса Машины.
        """
        super().__init__(label, mod, capacity, fuel_cap, fuel_cons, max_speed, color)


class Airplanes:  # Создаем класс "Самолеты"

    def __init__(self,
                 label: str = '',
                 mod: str = '',  # modifications (тип самолета)
                 fuel_cap: int = '',  # fuel_capacity (объём бака)
                 max_speed: int = '',
                 range_miles: int = '',
                 weight: int = '',
                 seats: int = '',
                 color: str = 'белый',
                 ):
        """
        Создаем конструктор класса.
        Конструктор вызывается автоматически при создании нового объекта класса
        с указанием базовых атрибутов, описанных в конструкторе.
        """
        self.label = label
        self.mod = mod
        self.fuel_cap = fuel_cap
        self.max_speed = max_speed
        self.range_miles = range_miles
        self.weight = weight
        self.seats = seats
        self.color = color  # Базовый цвет берется из указанных парамертов в конструкторе

        self._curr_speed = 0
        self.time_travel = 0
        self._travel_distance = 6468
        self._tickets = 0

        print('Запускаем производство самолетов.\n')

    def info(self):
        """
        Создаём функцию, выводящую информацию об объектах класса.
        Т.к. функция находится в родительском классе,
        Она может быть вызвана в дочерних классах.
        """
        print(
            f'Начинаем выпуск самолетов {self.label}.\n'
            f'Модификация - {self.mod}.\n'
            f'Максимальный объём топливного бака - {self.fuel_cap} литров.\n'
            f'Максимальная скорость - {self.max_speed}.\n'
            f'Максимальная дальность полёта - {self.range_miles} км.\n'
            f'Вес самолёта - {self.weight} тонн.\n'
            f'Количество пассажирских сидений - {self.seats} мест.\n'
            f'Базовый окрас - {self.color}.\n'
        )

    def travel(self):
        """
        Создаём функцию, определяющую время путешествия при средней скорости самолёта.
        Т.к. функция находится в родительском классе,
        Она может быть вызвана в дочерних классах.
        """

        self.time_travel = self._travel_distance / (self.max_speed / 2)
        print(f'Пассажирский самолёт фирмы {self.label} отправляется в Пекин. '
              f'Среднее время прибытиия - {round(self.time_travel)} часов. '
              f'Приятного полёта!')


class Boeing747(Airplanes):
    def __init__(self, label='Boeing747', mod='400', fuel_cap=214_140, max_speed=988, range_miles=14_205, weight=183,
                 seats=624):
        super().__init__(label, mod, fuel_cap, max_speed, range_miles, weight, seats)


class Boeing777(Airplanes):
    def __init__(self, label='Boeing777', mod='300', fuel_cap=181_280, max_speed=965, range_miles=14_685, weight=156,
                 seats=550):
        super().__init__(label, mod, fuel_cap, max_speed, range_miles, weight, seats)


class Airbus(Airplanes):
    def __init__(self, label='Airbus', mod='A340_600', fuel_cap=204_500, max_speed=890, range_miles=14_600, weight=177,
                 seats=520, color='малиновый'):
        super().__init__(label, mod, fuel_cap, max_speed, range_miles, weight, seats, color)

    def tickets(self, add_tickets: int):
        self._tickets = self._tickets + add_tickets
        if self._tickets < self.seats:
            print(f'Вы можете забронировать место на рейс! '
                  f'Забронировано {self._tickets} мест, осталость - {self.seats - self._tickets} мест.')
        if self._tickets == self.seats:
            print(f'Все места забронированы. Общее количество мест - {self.seats}')


def main():
    """
Создаём основную функцию для вывода атрибутов родительских/дочерних классов.
    """
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
    air_747 = Boeing747()
    air_747.info()
    air_747.travel()
    print()
    air_777 = Boeing777()
    air_777.info()
    air_777.travel()
    print()
    air_airbus = Airbus()
    air_airbus.info()
    air_airbus.travel()
    air_airbus.tickets(450)


# Сделать коллекцию из объектов и через цикл вызвать те методы, которые есть в обоихх классах.


if __name__ == '__main__':
    main()
