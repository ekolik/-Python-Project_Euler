from itertools import permutations

divisors = [2, 3, 5, 7, 11, 13, 17]
sum = 0

for i in permutations('0123456789'):
    for j in range(len(divisors)):
        if int(i[j+1]+i[j+2]+i[j+3]) % divisors[j] != 0:
            break

    else:
        sum += int(''.join(i))

print(sum)