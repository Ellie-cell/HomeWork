my_dict = {'Anton' : 1987 , 'Anna' : 2005 , 'Nelly' : 1999}
print(my_dict)
print(my_dict['Anton'])
print(my_dict.get('Elena'))
my_dict.update({'Sonya' : 2002 ,
                'Danil' : 1991})
a = my_dict.pop('Anna')
print(a)
print(my_dict)

my_set = {1,2,1,2, 'Apple', False , 45.67}
print(my_set)
list_ = (12,3,6)
my_set.add(list_)
my_set.remove('Apple')
print(my_set)
