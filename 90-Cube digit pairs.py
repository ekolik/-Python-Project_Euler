from itertools import combinations

pairs = [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5), (3, 6), (4, 6), (8, 1)]


def valid(cube1, cube2):
    for x, y in pairs:
        if not (x in cube1 and y in cube2 or x in cube2 and y in cube1):
            return False
    return True


all_cubes = list(combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 6], 6))
count = 0

for i in range(len(all_cubes)):
    for j in range(i, len(all_cubes)):
        if valid(all_cubes[i], all_cubes[j]):
            count += 1

print(count)
