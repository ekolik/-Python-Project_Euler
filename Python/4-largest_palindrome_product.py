n = rawn = raw_input()
n = int (n)

def pal(m):
    pal_set = []
    j=100000
    while j > 0:
        pal_set.append(m/j)
        m-=(m/j)*j
        j/=10
    #print pal_set
    
    return pal_set

numbers = [raw_input() for i in range(n)]
for i in range (n):
    number = int (numbers[i])
    pal_set_number = pal(number)

    first_part = pal_set_number[0]*100 + pal_set_number[1]*10 + pal_set_number[2]
    second_part = pal_set_number[2]*100 + pal_set_number[1]*10 + pal_set_number[0]

    flag = 0
    while first_part > 100:
        num = first_part*1000 + second_part
        i = 100
        if num <= number:
            while i <= 999:
                #print num
                if num%i == 0:
                    if num/i < 1000:
                        #print i
                        print num
                        flag = 1
                        break
                i+=1
        if flag == 1:
            break
        first_part -=1
        first_part_set = pal(first_part)
        #print first_part_set
        second_part = first_part_set[5]*100 + first_part_set[4]*10 + first_part_set[3]

        
        
        
