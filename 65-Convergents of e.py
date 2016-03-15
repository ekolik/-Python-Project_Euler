limit = 100

e = [1]*limit
e[0] = 2
for i in range(int(limit/3)):
    e[i*3+2] = 2*(i+1)
#print(e)

res = 1
d = 0
for i in e[::-1]:
    r = res
    res = res*i+d
    d = r
print(sum(int(i) for i in str(res)))