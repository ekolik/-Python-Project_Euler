import math
n = rawn = raw_input()
n = int (n)

numbers = [raw_input() for i in range(n)]
for i in range (n):
    number = int (numbers[i])
    sum = 0
    n = 2
    
    a_1 = 0
    a_n = 1
    
    while a_n <= number:
        a_0 = a_1
        a_1 = a_n
        a_n = a_0 + a_1
        if (a_n <= number and a_n%2 == 0):
            sum = sum + a_n

    print sum
    
