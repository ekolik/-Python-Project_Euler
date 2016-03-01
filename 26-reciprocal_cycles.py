import math
limit = 1000

def sieve(limit):
    limit = 1000
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

    return factors


def reptend(num):
    remainders = []

    for i in range(1,num):
        remainders.append(pow(10,i)%num)
    if sorted(remainders) == list(range(1,num)):
        return True

primes = sorted(sieve(limit), reverse=True)
for number in primes:
    if reptend(number):
        print(number)
        break