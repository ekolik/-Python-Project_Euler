lmt = 10000000


def sieve(start, limit):
    factors = []
    a = [True] * limit
    a[0] = a[1] = False
    p = 2
    for j in range(p * p, limit, p):
        a[j] = False
    factors.append(p)

    for p in range(3, limit, 2):
        if a[p]:
            for j in range(p * p, limit, p):
                a[j] = False
            factors.append(p)

    for i in range(len(factors)):
        if factors[i] >= start:
            st = i
            break
    return factors[st:]

mx = 0
primes = sieve(2000, 5000)

for i in range(len(primes)-1, 0, -1):
    for j in range(i-1, 0, -1):
        a, b = primes[i], primes[j]
        if a*b < lmt:
            if (a-1)*(b-1)/(a*b) > mx:
                if sorted(list(str(a*b))) == sorted(list(str((a-1)*(b-1)))):
                    #print(a*b, a, b, i, j)
                    res = a*b
                    mx = (a-1)*(b-1)/(a*b)
                    break
print(res)