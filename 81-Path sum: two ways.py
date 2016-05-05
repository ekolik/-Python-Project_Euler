matr = [list(map(int, l.split(sep=','))) for l in open("81-input.txt").readlines()]
rows = len(matr)
cols = len(matr[0])

# last column dynamic processing
for i in range(rows - 2, -1, -1):
    matr[i][cols - 1] += matr[i + 1][cols - 1]

# last row dynamic processing
for j in range(cols - 2, -1, -1):
    matr[rows-1][j] += matr[rows - 1][j + 1]

# all other sells dynamic processing
for i in range(rows - 2, -1, -1):
    for j in range(cols - 2, -1, -1):
        matr[i][j] += min(matr[i + 1][j], matr[i][j + 1])

print(matr[0][0])