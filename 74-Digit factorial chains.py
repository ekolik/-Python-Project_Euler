import time
from math import factorial

start_time = time.time()
limit = 1000000
facts = []

for i in range(10):
    facts.append(factorial(i))
# print(facts)


def fact_sum(num):
    return sum(facts[int(i)] for i in str(num))


count = 0
for n in range(limit):
    chain = []
    while len(chain) < 65:
        if n not in chain:
            chain.append(n)
            n = fact_sum(n)
        else:
            break
    if len(chain) == 60:
        # print(st)
        count += 1

print(count)
print("--- execution time: %s seconds ---" % (time.time() - start_time))
