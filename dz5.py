# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# import math

# num = int(input('Введите число: '))
# sqic = int(input('Введите квадрат: '))

# sum = int(math.pow(num, sqic))
# print(sum)

#  Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

def sum_rec (num, num1):
    if num == 0:
        return num1
        
    else:
        return sum_rec(num-1,num1+1)
        

num = int(input('Введите число: '))
num1 = int(input('Введите число: '))

sum_rec(num,num1)

print(sum_rec(num,num1))
