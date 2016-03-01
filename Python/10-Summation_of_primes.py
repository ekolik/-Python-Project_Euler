import math
n = rawn = raw_input()
n = int (n)

def sieve (num):
    limit = max(num)
    limit += 2
    #print num
    factors = []
    a = [True]* limit
    a[0]=a[1]=False

    p = 2
    for j in range(p*p, limit, p):
        a[j] = False
    factors.append(p)
           
    for p in range (3, limit, 2):
        if a[p]:
            for j in range(p*p, limit, p):
                a[j] = False
            factors.append(p)

    #print factors
    numbers_sort = sorted(num)
    
    #print num
    
    sum = 0
    k = 0
    sum_final = []
    for i in range (len(num)):
        while (k < len(factors) and factors[k] <= numbers_sort[i]):
            sum += factors[k]
            k += 1
        sum_final.append(sum)
    #print sum_final
    for i in range (len(num)):
        for j in range (len(num)):
            if num[i] == numbers_sort[j]:
                print sum_final[j]
                break

    

numbers = [int(raw_input()) for i in range(n)]
sieve(numbers)
