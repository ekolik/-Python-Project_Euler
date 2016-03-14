count = 0

for k in range(1, 10):
    n = 1
    while len(str(pow(k,n))) == n:
        if len(str(pow(k,n))) == n:
            #print(k,n,pow(k,n))
            count += 1
        n += 1

print(count)
