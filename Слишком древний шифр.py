

for i in range(3, 21):

    password =[]

    for j in range(1, i) :
        for k in range(1, i):
            if i % (j + k) == 0 and j != k:
                a = sorted((j, k))


                if not a in password :
                    password.append(a)


    b= sum(password,[])
    print(*b)











