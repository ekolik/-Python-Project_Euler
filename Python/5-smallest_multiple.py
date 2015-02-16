import math
n = rawn = raw_input()
n = int (n)

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    all_n = n
    while all_n > 1:
        d = 2
        n = all_n
        while n > 1:
            while n % d == 0:
                factors.append(d)
                n /= d
            d = d + 1
            if d*d > n:
                if n > 1:
                    factors.append(n)
                break
        all_n -= 1

    return factors


numbers = [raw_input() for i in range(n)]
for i in range (n):
    number = int (numbers[i])
    pfs = prime_factors(number)
    prod = math.factorial(number)
    
    for j in range (len(pfs)):
        temp = prod/pfs[j]
        flag = 0
        for k in range(2, number+1):
            if temp%k != 0:
                flag = 1
                break
        if flag == 0:
                prod = temp
            
        
    print prod
