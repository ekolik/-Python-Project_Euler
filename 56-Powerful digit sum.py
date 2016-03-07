curr_max = curr_a = curr_b = 0

for b in range(99, 90, -1):
    for a in range(99, 90, -1):
        curr_sum = sum(int(l) for l in str(pow(a, b)))
        if curr_sum > curr_max:
            curr_max = curr_sum
            curr_a = a
            curr_b = b

print(curr_max, curr_a, curr_b)