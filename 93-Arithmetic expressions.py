from operator import add, sub, mul, truediv
from itertools import permutations, product, combinations

mx = 0

for digitset in combinations(range(1, 10), 4):
    res = set()

    for item in permutations(digitset):
        for oper in list(product([add, sub, mul, truediv], repeat=3)):
            cand = oper[1](oper[0](item[0], item[1]), oper[2](item[2], item[3])) # (..)(..)
            if cand % 1 == 0 and cand > 0:
                res.add(int(cand))

            cand = oper[2](oper[1](oper[0](item[0], item[1]), item[2]), item[3]) # ((..).).
            if cand % 1 == 0 and cand > 0:
                res.add(int(cand))

            cand = oper[2](oper[0](item[0], oper[1](item[1], item[2])), item[3]) # (.(..)).
            if cand % 1 == 0 and cand > 0:
                res.add(int(cand))

            if not(oper[0] == truediv and oper[2](oper[1](item[1], item[2]), item[3]) == 0):
                cand = oper[0](item[0], oper[2](oper[1](item[1], item[2]), item[3])) # .((..).)
                if cand % 1 == 0 and cand > 0:
                    res.add(int(cand))

            if not(oper[0] == truediv and oper[1](item[1], oper[2](item[2], item[3])) == 0):
                cand = oper[0](item[0], oper[1](item[1], oper[2](item[2], item[3]))) # .(.(..))
                if cand % 1 == 0 and cand > 0:
                    res.add(int(cand))

    for i in range(1, max(res)):
        if i not in res:
            cur_mx = i-1
            break

    if cur_mx > mx:
        mx = cur_mx
        ans = item


print(''.join(str(i) for i in sorted(ans)))