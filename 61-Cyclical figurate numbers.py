from itertools import permutations

def triangle():
    trias = []
    for n in range(45, 141):
        trias.append(int(n*(n+1)/2))
    return trias


def square():
    squares = []
    for n in range(32, 100):
        squares.append(int(n*n))
    return squares


def pentagonal():
    pentas = []
    for n in range(26, 82):
        pentas.append(int(n*(3*n-1)/2))
    return pentas


def hexagonal():
    hexas = []
    for n in range(23, 71):
        hexas.append(int(n*(2*n-1)))
    return hexas


def heptagonal():
    heptas = []
    for n in range(21, 64):
        heptas.append(int(n*(5*n-3)/2))
    return heptas


def octagonal():
    octas = []
    for n in range(19, 59):
        octas.append(int(n*(3*n-2)))
    return octas


def cycle(first, second):
    heads = set()
    tails = set()

    for i in second:
        heads |= {str(i)[:2]}
    for i in first:
        tails |= {str(i)[2:]}

    #print(heads.intersection(tails))

    first_new = []
    for i in first:
        if str(i)[2:] in heads.intersection(tails):
            first_new.append(i)

    second_new = []
    for i in second:
        if str(i)[:2] in heads.intersection(tails):
            second_new.append(i)

    return [first_new, second_new]


all = [triangle(), square(), pentagonal(), hexagonal(), heptagonal(), octagonal()]
perms = list(permutations(range(6)))

for perm in perms:
    first_num, second_num = cycle(all[perm[0]], all[perm[1]])
    second_num, third_num = cycle(second_num, all[perm[2]])
    third_num, forth_num = cycle(third_num, all[perm[3]])
    forth_num, fifth_num = cycle(forth_num, all[perm[4]])
    fifth_num, sixth_num = cycle(fifth_num, all[perm[5]])
    sixth_num, first_num = cycle(sixth_num, first_num)

    while first_num and second_num and third_num and forth_num and fifth_num and sixth_num:
        first_num, second_num = cycle(first_num, second_num)
        second_num, third_num = cycle(second_num, third_num)
        third_num, forth_num = cycle(third_num, forth_num)
        forth_num, fifth_num = cycle(forth_num, fifth_num)
        fifth_num, sixth_num = cycle(fifth_num, sixth_num)
        sixth_num, first_num = cycle(sixth_num, first_num)

        if len(first_num)==len(second_num)==len(third_num)==len(forth_num)==len(fifth_num)==len(sixth_num)==1:
            print(first_num, second_num, third_num, forth_num, fifth_num, sixth_num)
            print(first_num[0]+second_num[0]+third_num[0]+forth_num[0]+fifth_num[0]+sixth_num[0])
            break

    else:
        continue
    break
