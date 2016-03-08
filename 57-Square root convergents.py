num, den, count = 3, 2, 0

for i in range(2, 1000):
    prev_num = num
    num += 2*den
    den += prev_num

    if len(str(num)) > len(str(den)):
        count += 1

print(count)