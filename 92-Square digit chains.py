import time, math

start_time = time.time()


def squared_digits(num):
    return sum(int(ch)**2 for ch in str(num))

res = 0
limit = 10000000
cachesize = int(81*math.log10(limit)) + 1
cache = [0]*cachesize

for i in range(1, cachesize):
    nxt = squared_digits(i)
    while nxt > i and nxt != 89:
        nxt = squared_digits(nxt)
    if cache[nxt] or nxt == 89:
        res += 1
        cache[i] = True

for i in range(cachesize, limit):
    if cache[squared_digits(i)]:
        res += 1

print(res)
print("--- execution time: %s seconds ---" % (time.time() - start_time))
