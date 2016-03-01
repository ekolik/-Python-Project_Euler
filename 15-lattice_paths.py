n = 20
res = 1
for i in range(1,n+1):
    res *= (n+i)/i

print(round(res))