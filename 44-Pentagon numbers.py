def is_pentagon(num):
    n = (24*num+1)**0.5 + 1
    if n%6 == 0:
        return True

not_found = True
i = 1

while(not_found):
    i += 1
    n = int(i*(3*i-1)/2)
    for j in range(i-1, 0, -1):
        m = int(j*(3*j-1)/2)
        if is_pentagon(n-m) and is_pentagon(n+m):
            not_found = False
            print(n-m)
            break