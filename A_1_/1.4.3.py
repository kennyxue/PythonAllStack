#coding:utf-8

def get_by_index_1(lst, i, value=None):
    if i < len(lst):
        return lst[i]
    else:
        return value

def get_by_index_2(lst, i, value=None):
    if -len(lst) <= i < len(lst):
        return lst[i]
    else:
        return value

def get_by_index_3(lst, i, value=None):
    try:
        return lst[i]
    except IndexError:
        return value
        
lst = [1, 2, 3]

while True:
    try:
        idx = int(input('input index of list:'))
    except ValueError:
        print("Index shoud be int.")
        continue
    value = input('input value:')

    if value != 'q':
         r1 = get_by_index_1(lst, idx, value)
         r2 = get_by_index_2(lst, idx, value)
         r3 = get_by_index_3(lst, idx, value)
         print(r1, r2, r3)
    else:
        break

