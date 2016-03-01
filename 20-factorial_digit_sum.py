n = 100
cur = 1
for i in range(1, n+1):
    while i%10 == 0:
        i /= 10
    cur = cur*int(i)

print(cur)

sum = 0
for j in str(cur):
    sum += int(j)

print(sum)

