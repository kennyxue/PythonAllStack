#coding:utf-8

nations = {'China':'Beijing', 'Japan':'Tokyo', 'India':'New Delhi', 'Sweden':'Stockholm', 'Russian':'Moscow', 'Germany':'Berlin', 'UK':'london', 'French':'Paris', 'Swiss':'Bern',
            'Egypt':'Cairo', 'Australia':'Canberra', 'New Zealand':'Wellington', 'Canada':'Ottawa', 'USA':'Washington', 'Cuba':'Havana', 'Brazil':'Brasilia'}
name = input('input a name of country:')
capital = nations.get(name)

print('the country:{0}, the capital:{1}'.format(name, capital))
