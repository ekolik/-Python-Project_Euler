# https://en.wikipedia.org/wiki/Partition_%28number_theory%29#Generating_function

k = sum([[int(i*(3*i - 1)/2), int(i*(3*i - 1)/2 + i)] for i in range(1, 250)], [])
limit = int(1e6)
p = [1]
n = 0
sign = [1, 1, -1, -1]

while p[n] > 0:
    n += 1
    i = 0
    pn = 0
    while k[i] <= n:
        pn += p[n - k[i]] * sign[i % 4]
        i += 1
    p.append(pn % limit)

print(n)
