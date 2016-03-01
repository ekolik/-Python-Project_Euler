with open("18-input") as f:
    content = f.readlines()

tria = list()

for i in range(len(content)):
    tria.append(content[i].split())
    for j in range(len(tria[i])):
        tria[i][j] = int(tria[i][j])

for i in range(len(content)-2, -1, -1):
    for j in range(len(tria[i])):
        tria[i][j] += max(tria[i+1][j], tria[i+1][j+1])

print(tria[0][0])