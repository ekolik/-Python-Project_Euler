import math
n = rawn = raw_input()
n = int (n)


numbers = [raw_input() for i in range(n)]
for i in range (n):
    number = int (numbers[i])
    half_n = int (math.sqrt(number/2))
    flag=0
    max=0
    for k in range(1,int(number/4)):
        half_n = int (math.sqrt(number/(2*k)))
        for m in range(half_n, 0, -1):
            for n in range(m-1, 0, -1):
                #print m,n
                if (2*m*k*(m+n)) == number:
                    if int(2*m*n*math.pow(k,3)*(math.pow(m,4)-math.pow(n,4))) > max:
                        max = int(2*m*n*math.pow(k,3)*(math.pow(m,4)-math.pow(n,4)))
    if max == 0:
        print -1
    else:
        print max
