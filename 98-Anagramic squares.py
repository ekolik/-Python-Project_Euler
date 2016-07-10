from itertools import permutations


def is_square(wrd):
    x = int(''.join(perm[letter_set[i]] for i in wrd))
    return x if int(x**0.5)**2 == x else False

words = []
for w in open("98-input.txt").read().split(','):
    if len(w) > 6:
        words.append((w[1:-1], sorted(w[1:-1])))

anagrams = []
while words:
    w = words.pop()
    anagrams += ((w[0], a[0]) for a in words if w[1] == a[1])

res = 0
for w, a in anagrams:
    letter_set = {x: y for y, x in enumerate(set(w))}
    for perm in permutations('123456789', len(letter_set)):
        if is_square(w) and is_square(a):
            res = max(is_square(w), is_square(a), res)
print(res)
