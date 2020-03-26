#coding:utf-8

skills = {'python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
myskill = {'python', 'Java'}

r = myskill & skills #.intersection

print(r)
print(bool(r))