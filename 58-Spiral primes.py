import time
import random
import sys
start_time = time.time()


def is_prob_prime(n, k=7):
    if n < 6:  # assume n >= 0 always
        return [False, False, True, True, False, True][n]
    elif n & 1 == 0:  # faster than n%2
        return False
    else:
        s, d = 0, n-1
        while d & 1 == 0:
            s, d = s+1, d >> 1  # equal to d/2
        for a in random.sample(range(2, min(n-2, sys.maxsize)), min(n-4, k)):
            x = pow(a, d, n)
            if x != 1 and x+1 != n:
                for r in range(1, s):
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    elif x == n-1:
                        a = 0  # so we know the loop didn't come to end
                        break
                if a:
                    return False
        return True


l = 3
nprimes = 3
ntot = 5

while True:
    dia = []
    dia1 = l*l + l + 1
    l += 1
    nprimes += sum(is_prob_prime(dia1 + i*l) for i in range(3))
    l += 1
    ntot += 4

    if nprimes/ntot < 0.1:
        print(l)
        break

print("--- execution time: %s seconds ---" % (time.time() - start_time))
