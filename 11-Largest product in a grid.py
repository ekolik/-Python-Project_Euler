


len = 20

board = [[j for j in raw_input().split()] for i in range(len)]
for i in range (len):
    for j in range (len):
        board[i][j] = int(board[i][j])
#print board
max = 0


for i in range(len):
    for j in range(len - 3):
        prod = board[i][j]*board[i][j+1]*board[i][j+2]*board[i][j+3]
        if max < prod:
            max = prod

for i in range(len - 3):
    for j in range(len):
        prod = board[i][j]*board[i+1][j]*board[i+2][j]*board[i+3][j]
        if max < prod:
            max = prod

for i in range(len - 3):
    for j in range(3, len):
        prod = board[i][j]*board[i+1][j-1]*board[i+2][j-2]*board[i+3][j-3]
        if max < prod:
            max = prod

for i in range(len - 3):
    for j in range(len - 3):
        prod = board[i][j]*board[i+1][j+1]*board[i+2][j+2]*board[i+3][j+3]
        if max < prod:
            max = prod

print max
