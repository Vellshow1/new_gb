
# ; В некоторой школе решили набрать три новых
# ; математических класса и оборудовать кабинеты для
# ; них новыми партами. За каждой партой может сидеть
# ; два учащихся. Известно количество учащихся в
# ; каждом из трех классов. Выведите наименьшее
# ; число парт, которое нужно приобрести для них.
# ; Input: 20 21 22(ввод чисел НЕ в одну строку)

# a =int(input('Введите число, учеников в классе: '))
# b =int(input('Введите число, учеников в классе: '))
# c =int(input('Введите число, учеников в классе: '))
# sum=(a+b+c)
# if sum // 2 ==0:
#     print(sum/2)
# else:
#     print(sum//2+1)

import random
# a = int(input('Введите кол-во дней: '))

# i = 0
# max =0
# max_max1 = list()
# max_max=0
# for i in range(int(a)):
#     max_max1.append(random.randint(-50,50))
#     print(max_max1, end=" ")
# for i in range(int(a)):
#     if(int(max_max1[i])>0):
#         max_max +=1
#     else:
#         if(max_max> max):
#             max = max_max
#         max_max =0
# print(max)

# a = int(input('Введите кол-во арбузов: '))

# numbers= list()

# for i in range(int(a)):
#     numbers.append(random.randint(1, 20))
# print(numbers)

# min = numbers[0]
# max = numbers[0]

# for i in range(int(a)):
#     if max < numbers[i]:
#         max = numbers[i]
#     elif min > numbers[i]:
#         min = numbers[i]
# print(f'Минимальный килограм арбуза: {min}, а максимальный {max}')

a = [1,3,4,5,6,7,8]
c = 2
print(a[c*-1:])