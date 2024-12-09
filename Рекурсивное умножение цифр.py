def get_multiplied_digits(number) :
    str_number = str(number)

    if len(str_number) == 1 :
        last_number = int(str_number)

        if last_number == 0:
            return 1
        else :
            return last_number


    else :
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)
