import math
n = rawn = raw_input()
n = int (n)

def sieve (num):
    limit = 10000000
    #print limit
    factors = []
    a = [True]*limit
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
    for i in range (len(numbers)):
        print factors[int(numbers[i])-1]
    #print factors
    
    

numbers = [raw_input() for i in range(n)]
sieve(numbers)
