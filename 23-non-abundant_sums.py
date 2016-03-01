import math
n = 28123


def sum_div(num):
    if num == 1:
        return 0
    else:
        r = math.floor(math.sqrt(num))
        if r*r == num:
            sum = 1 + r
            r -= 1
        else:
            sum = 1
        if num%2 != 0:
            f = 3
            step = 2
        else:
            f = 2
            step = 1
        while f <= r:
            if num%f == 0:
                sum += f + int(num / f)
            f += step
        return sum

abun = []
for i in range(1,n):
    if i < sum_div(i):
        abun.append(i)

sums = set()
for i in range(len(abun)):
    for j in range(i, len(abun)):
        if abun[i]+abun[j] >= n:
            break
        sums |= {abun[i]+abun[j]}


sum_abun = sum(sums)
all = int(n*(n-1)/2)

print(all - sum_abun)
