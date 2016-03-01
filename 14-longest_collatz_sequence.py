import time
start_time = time.time()
n = 1000000
cache = [0]*n
cache[0] = 1
max = 1
for i in range(2, n):
    curr = i
    count = 1
    while curr != 1:

        if int(curr)<i:
            count -= 1
            count += cache[int(curr)-1]
            break
        elif curr%2:
            curr = curr*3+1
        else:
            curr /= 2
        count +=1
    cache[i-1] = count
    if count >= max:
        max = count
        max_num = i
print("the starting number %s produces the longest chain of %s terms." % (max_num, max))
print("--- execution time: %s seconds ---" % (time.time() - start_time))