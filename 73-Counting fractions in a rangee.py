import time
from collections import Counter
start_time = time.time()

# --------------------------this part is taken from #71---------------------- #
limit = 12000
loc_a = 0
loc_b = 1
low_bound = 0
b = limit

while b > low_bound:
    # see https://en.wikipedia.org/wiki/Farey_sequence#Farey_neighbours
    if (b-1) % 3 == 0:
        a = int((b-1)/3)
        if loc_a * b < loc_b * a:
            loc_a = a
            loc_b = b
            low_bound = loc_b / (loc_b - 3*loc_a)
    b -= 1
# --------------------------------------------------------------------------- #
#print(loc_a, loc_b)

def farey(n):
    a, b, c, d = loc_a, loc_b,  1, 3     # (*)
    count = -1
    while c <= n:
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        count += 1
        if c == 1 and d == 2:
            break

    return count

print(farey(limit))

print("--- execution time: %s seconds ---" % (time.time() - start_time))