### by elimination, only left (10*a+b) / (10*b+c) = a / c,
### where a < c < b

from fractions import gcd

prod_n = 1
prod_d = 1

for b in range(1,10):
    for c in range(1, b):
        for a in range(1, c):
            if (10*a+b)*c == (10*b+c)*a:
                prod_n *= a
                prod_d *= c

print(int(prod_d/gcd(prod_n, prod_d)))