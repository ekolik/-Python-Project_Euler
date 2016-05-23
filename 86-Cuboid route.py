from math import sqrt

a = 2
tgt = 1000000
count = 0

while count < tgt:
    a += 1
    for bc in range(2, 2 * a + 1):
        cur = sqrt(a**2 + bc**2)
        if int(cur) == cur:
            if bc <= a:
                count += bc // 2
            else:
                count += a - (bc + 1)//2 + 1

print(a)