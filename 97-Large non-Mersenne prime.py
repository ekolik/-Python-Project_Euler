import time
start_time = time.time()

res = (28433*pow(2, 7830457, 10**10) + 1)%(10**10)
print(int(res))

print("--- execution time: %s seconds ---" % (time.time() - start_time))