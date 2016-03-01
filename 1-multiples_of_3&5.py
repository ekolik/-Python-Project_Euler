import math
n = rawn = raw_input()
n = long (n)

board = [raw_input() for i in range(n)]
#print board

for i in range (n):
    num = long (board[i])
    sum = long(0)
    num3=num5=num15=num
    if (num3%3 == 0 and num3 != 0):
        num3=num3-3
    if (num5%5 == 0 and num5 !=0):
        num5=num5-5
    if (num15%15 == 0 and num15 !=0):
        num15=num15-15
    while num3%3 != 0:
        num3=num3-1
    while num5%5 != 0:
        num5=num5-1
    while num15%15 != 0:
        num15=num15-1
    sum = (3+num3)*num3/6+(5+num5)*num5/10-(15+num15)*num15/30
    print sum
