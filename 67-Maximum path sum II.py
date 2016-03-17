# the algorithm is identical to the one for the problem 18

tria = [list(map(int, l.split())) for l in open("67-input.txt").readlines()]

for i in range(len(tria)-2, -1, -1):
    for j in range(len(tria[i])):
        tria[i][j] += max(tria[i+1][j], tria[i+1][j+1])

print(tria[0][0])