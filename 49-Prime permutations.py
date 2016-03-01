from itertools import permutations, combinations
limit = 10000

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

    for i in range(len(factors)):
        if factors[i] >= 1000:
            start = i
            break
    return factors[i:]


def arith_seq(a, b, c):
    arr = [a,b,c]
    arr.sort()
    return arr[1]-arr[0] == arr[2] - arr[1] and arr[0] != arr[1] != arr[2]



primes = sieve(limit)
for num in primes:
    perm_arr = []
    for p in permutations(str(num)):
        perm = int(''.join(p))
        if perm >= 1000 and perm in primes:
            perm_arr.append(perm)

    for c in combinations(perm_arr, 3):
        if arith_seq(c[0], c[1], c[2]) and c[0] != 1487:
            print(str(c[0])+str(c[1])+str(c[2]))
            break


    # for p in perm_arr:
    #     if p != 1487:
    #         for i in range(1, 4500):
    #             if p+i in perm_arr and p+2*i in perm_arr:
    #                 print(str(p)+str(p+i)+str(p+2*i))
    #                 break
    #         else:
    #             continue
    #         break
    else:
        continue
    break
