#coding:utf-8
'''
c^2 = a^2 + b^2 - 2abcosC
'''
import math

a = 3
b = 7
c = 9

cosC = (a**2 + b**2 -c**2) / (2*a*b)
C = math.acos(cosC)
print(C)