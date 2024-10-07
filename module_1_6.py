#Словари
my_dict = {'Владимир': 1989, 'Иван': 1990, 'Мария': 1995}
print(my_dict)
print(my_dict['Мария'])
print(my_dict.get('Петр', 'Такого человека нет в базе'))
my_dict['Игорь'] = 1956
my_dict.update({'Анна': 1992, 'Ксения':1993})
print(my_dict.pop('Иван'))
print(my_dict)

#Множества
my_set = {1, 1, 'one', 'one', True, (1,True,"str")}
print(my_set)
my_set.add(123)
my_set.update([456,799])
my_set.remove((1,True,"str"))
print(my_set)