import math
n = 10000


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

res = 0
for a in range(2, n):
    b = sum_div(a)
    if b > a:
        if sum_div(b) == a:
            res += (a+b)
print(res)