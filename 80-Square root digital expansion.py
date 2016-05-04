from decimal import *
getcontext().prec = 102

tot_sum = 0
for n in range(2, 100):
    d = Decimal(n).sqrt()
    if str(d)[2:]:
        #print(n, str(d)[2:101])
        tot_sum += sum(int(i) for i in str(d)[2:101])
        tot_sum += int(str(d)[0])
        #print(tot_sum)
print(tot_sum)