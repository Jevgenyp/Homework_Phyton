# Урок 1. Ввод-Вывод, операторы ветвления
# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# print('Введите день недели')
# day = int(input())
# if day > 0 and day <= 5:
#     print('нет.')
# if day > 5 and day < 8:
#     print('да')
# if day < 1 or day > 7:
#     print('Такого дня недели не существует.')

# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in [True, False]:
#     for y in [True, False]:
#         for z in [True, False]:
#             print(x, 'OR', y, 'OR', z, '=', x and y and z)
    
# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3 

# x = int(input('Введите X '))
# y = int(input('Введите Y '))
# if x != 0 and y != 0:
#     if x < 0 and y < 0:
#         print ('Точка находиться в 3ей четверти -X-Y')
#     elif x > 0 and y > 0:
#          print ('Точка находиться в 1ой четверти XY')
#     elif x > 0 and y < 0:
#          print ('Точка находиться в 4ой четверти X-Y')
#     elif x < 0 Mnd y > 0:
#          print ('Точка находиться в 2ой четверти -XY')
# else:
#     print ('Точка находиться в центре')


# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# quarter = int(input('Введите номер четверти: '))
# if quarter == 1:
#     print('диапазон возможных координат точек в этой четверти будет где: x > 0  и y > 0.')
# if quarter == 2:
#     print('диапазон возможных координат точек в этой четверти будет где: x < 0  и y > 0.')
# if quarter == 3:
#     print('диапазон возможных координат точек в этой четверти будет где: x < 0  и y < 0.')
# if quarter == 4:
#     print('диапазон возможных координат точек в этой четверти будет где: x > 0  и y < 0.')


# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# def toFixed(f: float, n=0): #сокращает количество цифр после запятой, не округляя!
#     a, b = str(f).split('.')
#     return '{}.{}{}'.format(a, b[:n], '0'*(n-len(b)))

# distAB = 0
# print('Введите координаты точки АX')
# ax = int(input())
# print('Введите координаты точки АY')
# ay = int(input())
# print('Введите координаты точки BX')
# bx = int(input())4
# print('Введите координаты точки BY')
# by = int(input())
# distAB  = ((bx - ax) ** 2) + ((by - ay) ** 2)
# distAB = distAB ** (0.5)
# print(toFixed(distAB, 2))


# 6. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# n = input('Введите число N: ')
# sum = 0
# for i in n:
#     if i != ',' and i != '.':
#         sum += int(i) 
# print(sum)


# 7. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# Факториал

# n = int(input('Введите число N:'))
# f = 1
# for i in range(1,n + 1):
#     f *= i
#     print(f, end = ' ')


# 8. Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input("введите целое число:\n"))
# nList = []

# nSum = 0
# for i in range(1, n + 1):
#     nList = [round(((1 + 1/i)**i),2) for i in range (1, n+1)]
#     nSum += round((1 + 1/n) ** n, 2)
# print(fr'Для числа n = {n} сумма последовательности (1 + 1\n)^n: {nList}'f'\n Сумма чисел = {nSum}')

  
    

    
    


