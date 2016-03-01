from math import pow
sum = 0
for i in range(1, 1001):
    mult = 1
    for j in range(1, i+1):
        mult *= i
        if mult >= pow(10,10):
            mult %= pow(10,10)
    sum += mult
    if sum > pow(10,10):
        sum %= pow(10,10)
print(sum)