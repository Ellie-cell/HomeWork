#Функция с параметрами по умолчанию:

def print_parms( a= 1, b = 'stroka', c = True) :
    print(a, b, c)

print_parms()
print_parms(b = 25)
print_parms( c = [1, 2, 3])
print_parms(a = 45.11, c = 'summer')

#Распаковка параметров:

values_list = [1, 'winter', False]
values_dict = { 'a' : 0.5, 'b' : 'SIDNEY', 'c' : True}

print_parms(**values_dict)
print_parms(*values_list)
print_parms(values_list, 34)
print_parms(values_dict, 88, 79)

#Распаковка + отдельные параметры:

values_list_2 = [23.19, 'photo']

print_parms(*values_list_2, 42)