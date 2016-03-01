limit = 1000000
start = 100000

def sieve(start, limit):
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
        if factors[i] >= start:
            st = i
            break
    return factors[st:]


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


def family8(num, dig):
    res = [num]
    count = 1
    for r in range(dig+1, 10):
        num2 = str(num).replace(str(dig), str(r))
        if is_prime(int(num2)):
            count += 1
            res.append(int(num2))
            if count == 8:
                print(res)
                return True
    return False


primes = sieve(start, limit)

for num in primes:
    for i in range(3):
        if str(num).count(str(i)) == 3 and str(num)[-1] != str(i):
            if family8(num, i):
                break
