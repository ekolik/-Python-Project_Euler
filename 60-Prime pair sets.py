lmt = 10000


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


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i*i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6
    return True


def conc_with(num, arr):
    res = []
    for pr in arr:
        if pr > num:
            if is_prime(int(str(pr)+str(num))) and is_prime(int(str(num)+str(pr))):
                res.append(pr)
    return res

primes = sieve(lmt)

for i in primes:
    i_arr = conc_with(i, primes)

    for ii in i_arr:
        ii_arr = conc_with(ii, i_arr)

        for iii in ii_arr:
            iii_arr = conc_with(iii, ii_arr)

            for iv in iii_arr:
                iv_arr = conc_with(iv, iii_arr)

                for v in iv_arr:
                    print(i, ii, iii, iv, v)
                    print(i+ii+iii+iv+v)
