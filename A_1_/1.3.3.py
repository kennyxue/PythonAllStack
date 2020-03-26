#coding:utf-8

s = 'Life is short You need Python'

for word in s.split():
    print(word,': ', word.lower(),', ', word.upper(),', ', len(word))

print([[word,': ', word.lower(), word.upper(), len(word)] for word in s.split()])