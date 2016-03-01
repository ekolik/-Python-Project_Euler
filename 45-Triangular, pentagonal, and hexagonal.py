from math import sqrt
n = 143

while True:
    n += 1
    hexa = n*(2*n-1)
    if ((1+sqrt(1+24*hexa))/6).is_integer():
        print(hexa)
        break