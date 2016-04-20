def sieve(limit):
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

    return factors


primes = sieve(1000)
target = 10

while True:
    ways = [0] * (target + 1)
    ways[0] = 1
    for i in primes:
        for j in range(i, target+1):
            ways[j] += ways[j - i]
    if ways[target] > 5000:
        print(target)
        break
    target += 1
