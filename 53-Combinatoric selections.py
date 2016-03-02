from math import factorial
def bigger(n, r):
    return int(factorial(n)/(factorial(r)*factorial(n-r))) > 1000000

count = 0
for n in range(1, 101):
    lcount = 0
    for r in range(1, int((n+1)/2)):
        if bigger(n, r):
            lcount += int((n+1)/2) - r
            break
    lcount *= 2
    if n%2 == 0:
        if bigger(n, int(n/2)+1):
            lcount += 1

    count += lcount
print(count)