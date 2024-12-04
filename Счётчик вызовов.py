calls = 0

def count_calls() :
     global  calls
     calls +=1

def string_info(string):
    a = str(string)
    result = (len(a), a.upper(), a.lower())
    count_calls()
    return result

def is_contains(string, list_to_search) :
    b = str(string.lower())
    c = list(list_to_search)
    count_calls()
    for i in range(len(c)) :
        if str(c[i].lower()) == b :
            result = True
            break
        else :
            result = False
            continue
    return result

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)





