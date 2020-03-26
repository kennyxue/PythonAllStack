#coding:utf-8

def contain_any_1(seq, aset):
    for c in seq:
        if c in aset:
            return True
    return False

def contain_any_2(seq, aset):
    for item in filter(aset.__contains__, seq):
        return True
    return False

def contain_any_3(seq, aset):
    return bool(aset.intersection(seq))

seq = "apython"
aset = set(list('abcde'))

result1 = contain_any_1(seq, aset)
print(result1)

result2 = contain_any_2(seq, aset)
print(result2)

result3 = contain_any_3(seq, aset)
print(result3)