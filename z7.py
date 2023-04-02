# import math
# num = int(input('Введите число: '))
# pow_num = int(input('Введите степень чила: '))

# print(int(math.pow(num, pow_num)))

# num = int(input('Введите число: '))

# sum = 0
# for i in range(num+1):  
#         sum = sum + i
    
# print(sum)

# color = int(input('Введите кол-во цветов, бусин: '))

# if color <= 1:
#     print('Минимальное кол-во, цветов бусин 2 шт')
# else:
#     print(f'минимальное кол-во бусин:{color+color}')


# import random
# a = int(input('Введите кол-во: '))
# array = []
# for i in range(1,a):
#     array.append(random.randint(1,5))
# print(array)
# count = 0

# i = 1

# while i < len(array)-1:
#     if array[i-1] < array[i] and array[i] > array[i+1]:
#         count+=1
#         i+=1
#     else:
#         i+=1
        
# print(count)



# array_one =[1,23,4,2,5,4,1,7]
# array_two = [2,3,4,2,1,5,53,5]
# array_tree = []
# sum = []

# for i in range(len(array_one)):
#     count = 0
#     for j in range(len(array_two)):
#         if array_one[i] == array_two[j]:
#             count +=1
#     if count == 0:
#         array_tree.append(array_one[i])
        
# print(array_tree)

# def speed_sort ( array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     min = [i for i in array[1:] if i <= pivot]
#     max = [i for i in array[1:] if i> pivot]
#     return speed_sort(min) + [pivot] + speed_sort(max)
    
# print(speed_sort([0,11,4]))

# array_1 = [1,3,4,52,1]
# array_2 = [2,3,4,5,1]
# array_3 =([i for i in array_1 if array_1[i] not in array_2[i]])
# print(array_3)

n = int(input())
Array = [1,2,3,4,5,6,7,8,9]
i = 0

if n >9:
    print(f'Введите число в от 1 до 9')
else:   
    while i < len(Array):
        if Array[i] == n:
            Array[i] = 'x'
            i+=1
        else:
            i+=1
    print(f'{Array[0]}|{Array[1]}|{Array[2]}')
    print(f'{Array[3]}|{Array[4]}|{Array[5]}')
    print(f'{Array[6]}|{Array[7]}|{Array[8]}')


def number(Array, n):
    if 'x' != Array:
        n = int(input())
        return n
    return Array
    
number(Array, n)