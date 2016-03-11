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
        m += 1
    for i in range(len(digits)):
        if Counter(digits)[digits[i]] == 5:
            print(nums[i])
            break
    else:
        n = m
        continue

    break

print("--- execution time: %s seconds ---" % (time.time() - start_time))