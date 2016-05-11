import networkx as nx

matr = [list(map(int, l.split(sep=','))) for l in open("83-input.txt").readlines()]
rows = len(matr)
cols = len(matr[0])

g = nx.DiGraph()
for i in range(rows):
    for j in range(cols):
        neighbors = []
        for x, y in (-1, 0), (0, -1), (1, 0), (0, 1):
            if 0 <= i + x < rows and 0 <= j + y < cols:
                neighbors.append((i + x, j + y))
        for ix, jy in neighbors:
            g.add_edge((i, j), (ix, jy), weight=matr[ix][jy])

path = nx.dijkstra_path_length(g, source=(0, 0), target=(rows-1, cols-1)) + matr[0][0]
print(path)
