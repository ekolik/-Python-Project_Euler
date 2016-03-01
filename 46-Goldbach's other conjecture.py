from math import sqrt


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


primes = []
num = 1
not_found = True

while not_found:
    num += 2
    if is_prime(num):
        primes.append(num)
    else:
        for prime in primes:
            if (sqrt(int((num-prime)/2))).is_integer():
                break
        else:
            print(num)
            not_found = False