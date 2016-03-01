import time
start_time = time.time()

digits_all = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0
for pr in range(1234, 9876):
    for a in range(1, 98):
        if pr%a == 0:
            digits = []
            letters = str(pr)+str(a)+str(int(pr/a))
            if len(letters) == 9:
                for i in letters:
                    digits.append(int(i))
                if sorted(digits) == digits_all:
                    count += pr
                    break
print(count)


print("--- execution time: %s seconds ---" % (time.time() - start_time))