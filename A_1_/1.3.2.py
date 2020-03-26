#coding:utf-8

user_input = input('input something:')

if user_input.isdigit():
    n = float(user_input)
    print(n * 10)
elif user_input.isalpha:
    print(user_input + '@python')
else:
    print(user_input)

