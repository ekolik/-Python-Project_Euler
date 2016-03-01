n = pow(9,5)*6
final = 0
for i in range(10, n):
    sum = 0
    for l in str(i):
        sum += pow(int(l),5)
    if sum == i:
        final += i
print(final)