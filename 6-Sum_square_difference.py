import math
n = rawn = raw_input()
n = int (n)

numbers = [raw_input() for i in range(n)]
for i in range (n):
    number = int (numbers[i])

    sum = number*(number+1)/2
    #print sum
    sum_2 = number*(2*number+1)*(number+1)/6
    #print sum_2
    

    #for k in range (1,number):
    #    for l in range (k+1, number+1):
    #        sum += k*l

    #sum *= 2
    print (sum*sum - sum_2)
