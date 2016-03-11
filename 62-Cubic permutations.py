import time
start_time = time.time()

n = 345

while True:
    #print(n)
    curr = [n**3]
    m = n+1
    while len(str(m**3)) == len(str(n**3)):
        curr.append(m**3)
        m += 1

    for i in range(len(curr)):
        count = 0
        for j in range(i+1, len(curr)):
            if sorted(str(curr[i])) == sorted(str(curr[j])):
                count += 1
        if count == 4:
            print(curr[i])
            break
    else:
        n = m
        continue
    break

print("--- execution time: %s seconds ---" % (time.time() - start_time))