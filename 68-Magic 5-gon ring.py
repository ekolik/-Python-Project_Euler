# the solution is easily found by ananlysis on paper.
# this implementation is just for fun.

from itertools import permutations

perms = list(permutations(range(1, 11), 10))
res = []

for perm in perms:
    if min(perm[0:5]) == perm[0]:
        equals = perm[4] + perm[9] + perm[5]
        string = ''
        for i in range(4):
            curr = perm[i] + perm[5+i] + perm[6+i]
            string += str(perm[i]) + str(perm[5+i]) + str(perm[6+i])
            if curr != equals:
                break
        else:
            res.append(string + str(perm[4]) + str(perm[9]) + str(perm[5]))

print(max(res))