# Задание -8

#8 типов данных и примеры
# int_1 = int(2)
# str_1 = str('str')
# bol_1 = bool(True)
# flot_1 = float(4.45)
# lst = ['list', 145]
# set_1 = {'int','str', 'str'}
# dict_1 = {'itemss':
#     {'key': 'value0'}}
# tupl_1 = (1, 2, 3)

# print(type(int_1))
# print(type(str_1))
# print(type(bol_1))
# print(type(flot_1))
# print(type(lst))
# print(type(set_1))
# print(type(dict_1))
# print(type(tupl_1))


# Задание -7
# git клонировать адрес вашего проекта
# git push origin master
# git remote добавить источник адрес вашего проекта
# git remote -v


#  Задание -6
# как создать 2 папки одной командай 
# mkdir papka_1 papka_2

#  Задание -5
# как вывести на экран слово ПРИВЕТ МИР
# a = 'ПРИВЕТ МИР'
# print(a)


#  Задание -4
# как найти количество одинаковых значений внутри списка приведите примеры
# a = ['str', 12, 'str', 45, 'str']
# print(a.count('str'))


#  Задание -3
# как запросить bool от пользователя приведите примеры
# a = 15
# b = 18
# c = a - b
# if c > 0:
#     print(True)
# else:
#     print(False)
    

#  Задание -2
# как найти длину массива приведите примеры

# lst = ['str', 12, 'str', 45, 'str']
# print(len(lst))


# Задание -1
# from curses.ascii import isdigit
# a = input('Enter number: ')
# if a.isdigit() == True:
#     print(True)
# else:
#     print(False)


#  Задание 0
# получите сумму листа [7,8,8,4,8,4,8,4,8,4,8,4,8] 
# lst = [7,8,8,4,8,4,8,4,8,4,8,4,8] 
# print(sum(lst))


#  Задание 1
# Есть список:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Выведите все элементы, которые больше 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # print(a[5::1])
# b = []
# for i in a:
#     if i > 5:
#         b.append(i)
# print(b)


# Задание 2
# digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# for i in digits:
#    if i % 9==0:
#        print(i)


#Задание 3
# fruits = ['banana','stawberry','apple','orange','limon','ananas']
# print(fruits[0])
# print(fruits[-1])


# Задание 4
# spisok_1 = {'Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 1, 23}
# spisok_2 = {'Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23}
# a=spisok_1.intersection(spisok_2)
# print(a)


# Задание 5 
# for i in range(300):
#    if i %2==0:
#        print(i)
#    elif i ==237:
#        break


# Задание 6
# import random
# a = int(input('Введите число: '))
# num2 = random.randint(1,100)
# while  a != num2 :
#     num = int(input('>>> '))
#     if num2 > num:
#         print('Больше')
#     elif num2 < num:
#         print('Меньше')
#     elif num == num2:
#         print('Вы отгадали, КОНГРАТУЛЕЙШН')


# Задание 7 
# user = input('Введите свой логин: ')
# lst1 = ['erty','yuioki','ass']
# while True:
#     if user == 6:
#         lst1.append(user)
#         break
#     elif user != 6:
#         users = input('Введите 6 символов: ')
#         break
#     else:
#         break
#         print('Введите буквы!')
# print(' '.join(lst1))

# не работает


# Задание 8 

# numbers = [2,4,7,1,8.4,-3.3]
# num = [7.1,-2,4,-1,7,-43,8,-3,6,9]
# res = [i for i in numbers if not i % 2] 
# res2 = [i for i in num if i % 2]
# print(res)
# print(res2)


#  Задание 9 
# numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
# for i in numbers:
#     if i >= 0:
#         print(i)


# Задание 10 
# my_list = [2,4,6,8,10,1,3,5,7,9,11,13,17]
# print(my_list)
# for i in my_list:
#    if my_list.index(i) % 2 == 0:
#        print(i)


# Задание 11:
# Дан список чисел:
# numbers = [1,0,-2,4,3,6,6,3,5,8,4,2] 
# Выведите все элементы списка, которые больше предущего элемента
# Пример: (numbers: 1,5,2,4,3 Результат: 5,4)

# numbers = [1,0,-2,4,3,6,6,3,5,8,4,2] 
# numbers.sort(reverse= True)
# print(numbers)


# Задание 12
# a = "175315354518498331"
# b = a.count('3')
# print(b)


#  Задание 13
# a = (7+5) * 56 / (3 * (27 ** 3))
# a1 = 7+5
# a2 = 23 ** 3
# a3 = 3 * 12167
# a4 = 12 * 56
# a5 = 672 / 36501
# print(a)


# Задание 14
# modified = '''исследователи ESET с()()бщили/
# чт() в наст()ящее время активн()сть XDSpy прекратилась/
# и пр()из()шл() эт() п()сле предупреждения/ ()публик()ванн()г() бел()русским cert в феврале текущег() г()да!
# П() сути/ т()гда эксперты ()бнаружили ()дну из вред()н()сных кампаний хакер()в/ к()т()рая и была детальн() ()писана в д()кументе!
# именн() инф()рмация бел()русск()г() cert стала ()тправн()й т()чк()й для начала расслед()вания eset и п()м()гла аналитикам ()бнаружить пр()шлые ()перации XDSpy!'''
# a= modified.replace('()',"o")
# print(a)


# Задание 15
# list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# a = sum(list_1)
# b = sum(list_2)
# if a > b:
#     print(a)
# else:
#     print(b) 


# Задание 16
# y_friends = {
# "Joomart": "+996555246810", 
# "Adinai": "+996555013579",
# "Ermek": "+996777013579",
# "Atai": "+996777246810",
# "Aslan": "+996999246810",}
# his_her_friends = {
# "Lyazat": "+996551123456",
# "Salavat": "+996552234567",
# "Daniyar": "+996553345678",
# "Bolot": "+996554456789",
# "Alymbek": "+996555501234",
# "Dastan": "+996556678912",
# "Maksat": "+996557789012",
# "Aibek": "+996558890123",
# }
# y_friends.update(his_her_friends)
# print(y_friends)


# Задание 17
# a = input('text: ')
# a1 = a[:len(a) // 2]
# a2 = a[len(a) // 2:]
# print(a1.lower(), a2.upper())


# Задание 18 

# ch = 'абвгдеёжзийКклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# shifr = int(input('Шаг шифровки: '))
# step = input('Сообщение для ДЕшифровки: ').upper()
# itog = ''
# for i in step:
#     sh = ch.find(i)
#     shiff = sh + shifr
#     if i in ch:
#         itog += ch[shiff]
#     else:
#         itog += i
        
# print(itog)


# Задание 19
# c = {}
# num1 = input('Введите номер: ')
# num2 = input('Введите страну: ')
# c[num1] = 'num2'
# print(c)


# Задание 20
# Посчитайте сколько цифр 13 встречается в списке, сколько процентов 
# занимает цифра 13 в списке.
# если 13 больше 70% ответ 'я так и знал'
# если 13 меньше 70 % 'ответ неужели'
# если 13 = 70 % ответ 'совпадение ? не думаю'
# a = [1, 1, 2, 3,13, 13, 13, 13, 13, 13, 13, 13,
# 13, 5, 8, 13, 21, 34,1,55, 13, 13, 13, 13, 13, 
# 13, 13, 13, 13, 13, 13, 13, 1313, 13, 13, 13, 13, 13, 89]
# a.append(13)
# b = a.count(13) * 100 / len(a)
# if b == 70.0:
#         print('совпадение? не думаю')
# if b < 70.0:
#         print('неужели')
# if b > 70.0:
#         print('я так и знал')


#  Задание 21
# a = input('Введите длину: ')
# b = int(a)
# uslov = input('Площадь ил Периметр ?: ')
# if uslov == 'Площадь':
#     print(b * b)
# elif uslov == 'Периметр':
#     print(b * 4)


# Задание 22
# a = int(input('Расстояние: '))
# b = int(input('Скорость: '))
# c = a // b
# z = 60 // c
# print(f'За {z} часов будет преодолено {a}км растояния, при скорости {b}кмч')


# Задание 23:
# создайте lambda функцию для вычисления процента от 2022
# функция должна принимать 1 аргумент и 
# вернуть какой процент он состовляет от 2022
# результат округлите до 2 цифр осле запятой
# пример: 2022 = 100%; 100 = 4.94%; 1022 = 50.54%


# f = lambda b: f' = {b / 2022 * 100}%' 
# print(f(400))