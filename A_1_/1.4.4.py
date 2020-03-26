#coding:utf-8

import re

def select_numbers(s):
    pieces = re.compile(r'(\d+)').split(s)
    pieces[1::2] = map(int, pieces[1::2])
    return pieces

def sort_filename(filename):
    return sorted(filename, key=select_numbers)

files = ['py10.py', 'py2.py', 'py1.py', 'py14.py']
result = sort_filename(files)

print(files)
print(result)