res = 0


def same_row(i, j): return i//9 == j//9


def same_col(i, j): return (i - j) % 9 == 0


def same_block(i, j): return i // 27 == j // 27 and i % 9 // 3 == j % 9 // 3


def solve(pzl):
    global res
    i = pzl.find('0')
    if i == -1:
        res += int(pzl[0:3])
        print(res)
        return True

    excluded_numbers = set()
    for j in range(81):
        if same_row(i, j) or same_col(i, j) or same_block(i, j):
            excluded_numbers.add(pzl[j])

    for cand in '123456789':
        if cand not in excluded_numbers:
            solve(pzl[:i] + cand + pzl[i+1:])


file = open("96-input.txt").readlines()

puzzles = ''.join([line.strip() for line in file if 'Grid' not in line])
puzzles = [puzzles[i:(i+81)] for i in range(0, len(puzzles), 81)]

[solve(puzzle) for puzzle in puzzles]
print(res)
