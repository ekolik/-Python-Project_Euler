n = 0
d = 0
final = 1

for step in range(7):
    while d < pow(10, step):
        n += 1
        d += len(str(n))

    diff = d - pow(10, step)
    if diff:
        mult = int(str(n)[len(str(n)) - diff - 1])
    else:
        mult = int(str(n)[-1])

    final *= mult

print(final)