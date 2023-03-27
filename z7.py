list = input()

def newtext (list):
    if len(list) == 1 or len(list) == 2:
        return list
    return list[0] +'*' + newtext(list[1:-1]) + '*' + list[-1]

print(newtext(list))