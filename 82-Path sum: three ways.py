import numpy

matr = [list(map(int, l.split(sep=','))) for l in open("82-input.txt").readlines()]
rows = len(matr)
cols = len(matr[0])

m_up = [0]*rows
m_down = [0]*rows

for j in range(cols - 2, -1, -1):
    m_up[rows - 1] = matr[rows - 1][j] + matr[rows - 1][j + 1]
    for i in range(rows - 2, -1, -1):
        m_up[i] = matr[i][j] + min(m_up[i + 1], matr[i][j + 1])

    m_down[0] = matr[0][j]+ matr[0][j + 1]
    for i in range(1, rows):
        m_down[i] = matr[i][j] + min(m_down[i - 1], matr[i][j + 1])

    for i in range(0, rows):
        matr[i][j] = min(m_up[i], m_down[i])

print(min(numpy.array(matr)[:, 0]))
