# sum_array = [1,3,3,4]
# max_num = max(sum_array)
# min_sum = min(sum_array)

# print(f'Максимальная оценка: {max_num} и минимальная {min_sum}')

# for i in range(len(sum_array)):
#     if sum_array[i] == max_num:
#         sum_array[i] = 5
        
# print(sum_array)

list = [1,2,3,4,5,6]


i = 0 


while i < len(list):
    sum = 0
    sum = list[i]
    list[i] = list[i-1]
    list[i-1] = sum
    i+=1
print(list)