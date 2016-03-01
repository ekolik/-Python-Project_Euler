import time
start_time = time.time()

limit = 7654321
# the fastest one
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

# # second fastest
# def sieve(limit):
#     factors = []
#     a = [True] * limit
#     a[0] = a[1] = False
#
#     for n in range(2, int(limit**0.5 + 1.5)):
#         if a[n]:
#             for i in range(n*n, limit, n):
#                 a[i] = False
#             factors.append(n)
#
#     return [i for i, isprime in enumerate(a) if isprime]

primes = sieve(limit)

for i in range(len(primes)-1, -1, -1):
    stri = str(primes[i])
    if ''.join(sorted(stri)) == '123456789'[:len(stri)]:
        print(primes[i])
        break

# third fastest (function + the rest of the code)
# def sieve(limit):
#     a = [True] * limit
#     a[0] = a[1] = False
#
#     for (i, isprime) in enumerate(a):
#         if isprime:
#             yield i
#             for n in range(i*i, limit, i):
#                 a[n] = False
#
#
# for i in reversed(list(sieve(limit))):
#     stri = str(i)
#     if ''.join(sorted(stri)) == '123456789'[:len(stri)]:
#         print(i)
#         break



print("--- execution time: %s seconds ---" % (time.time() - start_time))