from collections import deque
import time
start_time = time.time()

limit = 1000000
final = 0


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


def all_rotations(number):
    rotations = set()
    d = deque(str(number))
    for i in range(len(d)):
        d.rotate(1)
        lst = ''
        for n in d:
            lst += str(n)

        rotations |= {int(lst)}

    return rotations


primes = sieve(limit)


while primes:
    p = primes[0]
    for l in str(p):
        if (int(l)%5 == 0 or int(l)%2 == 0) and p != 2 and p != 5:
            primes.remove(p)
            break
    else:
        rots = all_rotations(p)
        for r in rots:
            if r not in primes:
                primes.remove(p)
                break
        else:
            for r in rots:
                final += 1
                primes.remove(r)

print(final)
print("--- execution time: %s seconds ---" % (time.time() - start_time))