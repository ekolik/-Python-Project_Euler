import time
start_time = time.time()

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

l = 3
nprimes = 3
ntot = 5

while True:
    dia = []
    dia1 = l*l + l + 1
    l += 1
    nprimes += sum(is_prime(dia1 + i*l) for i in range(3))
    l += 1
    ntot += 4

    if nprimes/ntot < 0.1:
        print(l)
        break

print("--- execution time: %s seconds ---" % (time.time() - start_time))