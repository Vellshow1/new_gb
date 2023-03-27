# sum_array = [1,3,3,4]
# max_num = max(sum_array)
# min_sum = min(sum_array)

# print(f'Максимальная оценка: {max_num} и минимальная {min_sum}')

# for i in range(len(sum_array)):
#     if sum_array[i] == max_num:
#         sum_array[i] = 5
        
# print(sum_array)

# def palen (a):
#     if len(a) <=1:
#         return True
#     if a[0] != a[-1]:
#         return False
#     else:
#         return palen(a[1:-1])
    
# print(palen('шалашa'))

def newtext(list):
    if len(list) == 1 or len(list) == 2:
        return list
    return list[0] +'(' + newtext(list[1:-1]) +')' + list[-1]
    
list =input()
print(newtext(list))