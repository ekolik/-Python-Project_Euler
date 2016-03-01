def prime_factors(n):
    i = 2
    factors = []
    while i*i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def is_4primes(arr):
    return len(set(arr)) == 4


i = 2*3*5*7
not_found = True
step = 0

while not_found:
    for k in range(4):
        if not is_4primes(prime_factors(i+k)):
            step = k+1
            break
    else:
        print(i)
        not_found = False

    i += step
