import time
from collections import Counter
start_time = time.time()

n = 345

while True:
    nums = [n**3]
    digits = [''.join(sorted(str(nums[0])))]

    m = n+1
    while len(str(m**3)) == len(str(n**3)):
        nums.append(m**3)
        curr_digit = ''.join(sorted(str(m**3)))
        digits.append(curr_digit)

        if Counter(digits)[curr_digit] == 5:
            break
        m += 1
    else:
        n = m
        continue

    for i in range(len(nums)):
        if digits[i] == curr_digit:
            print(nums[i])
            break
    break

print("--- execution time: %s seconds ---" % (time.time() - start_time))