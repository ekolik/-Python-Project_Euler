import math
n = rawn = raw_input()
n = int (n)


numbers = [raw_input().split() for i in range(2*n)]
for i in range (0,n*2,2):
    digit = int(numbers[i][0])
    consec = int (numbers[i][1])
    number = numbers[i+1][0]
    #print int(number[0])

    max = 0
    for k in range (0,digit-consec):
        prod = 1
        for j in range (k,consec+k):
            prod *= int(number[j])
        if prod > max:
            max = prod

    print max
