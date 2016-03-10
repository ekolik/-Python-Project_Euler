from itertools import permutations


def formulae(m):
    result = []
    for n in range(19, 141):
        if m == 3:
            curr = int(n*(n+1)/2)
        elif m == 4:
            curr = int(n*n)
        elif m == 5:
            curr = int(n*(3*n-1)/2)
        elif m == 6:
            curr = int(n*(2*n-1))
        elif m == 7:
            curr = int(n*(5*n-3)/2)
        elif m == 8:
            curr = int(n*(3*n-2))

        if 999 < curr < 10000:
            result.append(curr)
    return result


def cycle(first, second):
    # rewrites 'first' and 'second' so that they are cyclical 'first->second'
    heads = {str(i)[:2] for i in second}
    tails = {str(i)[2:] for i in first}

    first_new = [i for i in first if str(i)[2:] in heads.intersection(tails)]
    second_new = [i for i in second if str(i)[:2] in heads.intersection(tails)]

    return [first_new, second_new]


all_poss = [formulae(i) for i in range(3, 9)]
perms = list(permutations(range(6)))

for perm in perms:
    # first, initializing step in creating 6 arrays, each cycles to the next
    first_num, second_num = cycle(all_poss[perm[0]], all_poss[perm[1]])
    second_num, third_num = cycle(second_num, all_poss[perm[2]])
    third_num, forth_num = cycle(third_num, all_poss[perm[3]])
    forth_num, fifth_num = cycle(forth_num, all_poss[perm[4]])
    fifth_num, sixth_num = cycle(fifth_num, all_poss[perm[5]])
    sixth_num, first_num = cycle(sixth_num, first_num)

    # continue cycling found arrays to eliminate non-six-length cycles
    while first_num and second_num and third_num and forth_num and fifth_num and sixth_num:
        first_num, second_num = cycle(first_num, second_num)
        second_num, third_num = cycle(second_num, third_num)
        third_num, forth_num = cycle(third_num, forth_num)
        forth_num, fifth_num = cycle(forth_num, fifth_num)
        fifth_num, sixth_num = cycle(fifth_num, sixth_num)
        sixth_num, first_num = cycle(sixth_num, first_num)

        if len(first_num) == len(second_num) == len(third_num) == len(forth_num) == len(fifth_num) == len(sixth_num) == 1:
            print(first_num, second_num, third_num, forth_num, fifth_num, sixth_num)
            print(first_num[0]+second_num[0]+third_num[0]+forth_num[0]+fifth_num[0]+sixth_num[0])
            break

    else:
        continue
    break
