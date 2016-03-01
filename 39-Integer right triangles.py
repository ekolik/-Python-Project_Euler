max = 0
for p in range(2, 1000, 2):
    count = 0
    for b in range(1, int(p/3)):
        if p*(p-2*b) % (2*p-2*b) == 0:
            count += 1
    if count > max:
        max = count
        final = p

print(final)