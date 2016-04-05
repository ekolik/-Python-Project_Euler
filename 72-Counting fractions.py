lmt = 1000000
phi = list(range(0, lmt+1))
res = 0

for i in range(2, lmt+1):
    if i == phi[i]:
        for j in range(i, lmt+1, i):
            phi[j] *= (1-1/i)
    res += int(phi[i])

print(res)