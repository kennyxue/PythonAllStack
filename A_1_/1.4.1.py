#coding:utf-8

def convert(word, low=True):
    if low:
        return word.lower()
    else:
        return word.upper()
w = "Physics"
print(convert(w))
print(convert(w, low=False))

