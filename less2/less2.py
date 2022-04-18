# создание трех переменных с одинаковыми данными и одинаковыми идентификаторами
print()
year = 2022
year2 = 2022
year3 = 2022
print(id(year))
print(id(year2))
print(id(year3))
# создание двух переменных с одинаковыми данными и разными идентификаторами
print()
number = [100]
number2 = [100]
print(id(number))
print(id(number2))
# изменение идентификации переменных
# Три переменные с одинаковыми даннымии разными идентификаторами
print()
print(id(year))
print(id(float(year2)))
print(id(str(year3)))
# Две переменные с одинаковыми данными и одинаковыми идентификаторами
print()
print(id(number))
print(id(int(number2)))