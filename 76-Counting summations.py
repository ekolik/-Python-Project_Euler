N = 100
ways = [0]*(N+1)
ways[0] = 1

for i in range(1, N):
    for j in range(i, N+1):
        ways[j] += ways[j - i]

print(ways[100])