print('\t\t\t Some text') #Табуляционный отстут \t
print()
print('Тут можно' + 'что-то написать.' + ' ' + 'Но это не точно.') # Конкатенация строк (склеивание)
print('Хочу есть!!'*10 + ' АааааааааааааааАААаааа!!!!!')
print()
name = 'Maks'
print('Hello '+name + '!!')
print()
#city = input('Enter the city')
#print(city)
print()
list = ['777', 811,[43,'elk',44],123456]
#print(list[2][1]) #обращение к 1 элементу второго(вложенного) списка.
list[0] = 123456
list[1] = 'Mortal'
print(list)
print(list.index(123456)) #Возвращает индекс числа 123456 в списке
print(list.count(123456)) #Djpdhfoftn количество повторов в списке
print('Mortal' in list) #Определяем слово "Mortal" в списке
print(44 in list[2]) # Определяем число 43 во слоденном списке с индексом 2
print()
p= [1, 135, 4, 98, 188, 744]
print(max(p))
print(len(p))
print(min(p))
print(136 not in p)
p.append(90)
print(p)
print()

a = [1,2, [9,8], 4]
print(a[2][1])