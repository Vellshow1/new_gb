# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# array = [1,2,5,3,6,7,9,54,9,0,5,2,1,6]

# min = int(input('Введите первое число диапозона: '))
# max = int(input('Введите второк число диапозона: '))

# for i in range(len(array)):
#     if min <= array[i] <= max:
#         print(i)



#  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# an = a1 + (n-1) * d.

array = []
a1 =int(input())
n = int(input())
d = int(input())
for i in range(n):
    array.append(a1+i*d)
    
print(array)