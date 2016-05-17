from random import randint


def cc(cpos, ccpile):
    cc_go = [0,10]
    ccpile = (ccpile + 1) % 16
    if ccpile < 2:
        cpos = cc_go[ccpile]
    return [cpos, ccpile]


def ch(cpos, chpile):
    ch_go = [0,10,11,24,39,5]
    chpile = (chpile + 1) % 16

    if chpile < 6:
        cpos = ch_go[chpile]
    elif chpile == 6 or chpile == 7:
        if cpos == 7:
            cpos = 15
        elif cpos == 22:
            cpos = 25
        elif cpos == 36:
            cpos = 5
    elif chpile == 8:
        cpos = 28 if cpos == 22 else 12
    elif chpile == 9:
        cpos -= 3
    return [cpos, chpile]


cpos = 0
ccpile = 0
chpile = 0
board = [0]*40
samples = 1000000
doubles = 0

for i in range(samples):
    # roll the dices
    dice1 = randint(1,4)
    dice2 = randint(1,4)

    # check doubles
    doubles = doubles + 1 if dice1 == dice2 else 0
    if doubles > 2:
        cpos = 10
        doubles = 0
    else:
        # move to the square
        cpos = (cpos + dice2 + dice1) % 40

        # handle chance
        if cpos == 7 or cpos == 22 or cpos == 36:
            cpos, chpile = ch(cpos, chpile)
        # handle cc
        if cpos == 2 or cpos == 17 or cpos == 33:
            cpos, ccpile = cc(cpos, ccpile)
        # handle go to jail
        if cpos == 30:
            cpos = 10

    board[cpos] += 1

print(board)
res = [i[0] for i in sorted(enumerate(board), key=lambda x:x[1], reverse=True)]
print(''.join(str(i) for i in res[:3]))