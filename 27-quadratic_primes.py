limit = 1000
max = 0


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num%2 == 0 or num%3 == 0:
        return False
    i = 5
    while i*i <= num:
        if num%i == 0 or num%(i+2) == 0:
            return False
        i += 6
    return True


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


primes = sieve(limit)

for a in range(-limit+1, limit, 2):
    for b in primes+[-i for i in primes]:
        a_even = 1 if b in [-2, 2] and a < limit-1 else 0
        n = 0
        while is_prime(n*n+(a+a_even)*n+b):
            n += 1
        if n > max:
            max = n
            final = a*b
print(final)