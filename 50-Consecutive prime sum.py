limit = 1000000

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

primes = sieve(limit)

sum_max = 0
count_max = 0
for prime in primes:
    if sum_max+prime < limit:
        sum_max += prime
        count_max += 1

num_final = 0

for i in range(count_max):
    for j in range(i+1):
        current = sum(primes[(i-j):count_max-j])
        if current in primes:
            count_final = count_max-i
            num_final = current
            break
    else:
        continue
    break

print(num_final)