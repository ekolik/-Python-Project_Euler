limit = 1001
first = 1
last = 1
sum = first
for n in range(2, limit, 2):
    first = last + n
    sum += 2*(2*first + 3*n)
    last = first + 3*n
print(sum)