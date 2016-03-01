from itertools import permutations
n = 1000000
letters = '0123456789'
p = permutations(letters)
p = enumerate(p)
for i in p:
    if i[0] == n-1:
        print(''.join(i[1]))
        break
