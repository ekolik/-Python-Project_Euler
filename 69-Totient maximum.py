# https://en.wikipedia.org/wiki/Euler's_totient_function#Euler.27s_product_formula

limit = 1000000

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

prod = 1
for prime in primes:
    prod *= prime
    if prod > limit:
        print(int(prod/prime))
        break
