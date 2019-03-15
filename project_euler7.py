def countPrime():
    a = []
    count = 0
    for number in range(1,1000):
        a.append(number)
        if number > 1:
            if number % number == 0: # insert factor counter here where factors are == 2
                while a.index(number) <= 1001:
                    print('number:',number,'index:',a.index(number))
                    break

countPrime()