n = rawn = raw_input()
n = int (n)

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors


numbers = [raw_input() for i in range(n)]
for i in range (n):
    number = int (numbers[i])
    pfs = prime_factors(number)
    largest_prime_factor = max(pfs) # The largest element in the prime factor list
    print largest_prime_factor
