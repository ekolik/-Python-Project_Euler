from itertools import product

def sieve(limit):
    factors = []
    a = [True] * limit
    a[0] = a[1] = False
    p = 2
    for j in range(p * p, limit, p):
        a[j] = False
    factors.append(p)

    for p in range(3, limit, 2):
        if a[p]:
            for j in range(p * p, limit, p):
                a[j] = False
            factors.append(p)

    return factors


lmt = 50000000
st = set()

for p in product(sieve(int(lmt**0.5)), sieve(int(lmt**(1/3))), sieve(int(lmt**(1/4)))):
    cur_sum = p[0]**2 + p[1]**3 + p[2]**4
    if cur_sum < lmt:
        st.add(cur_sum)

print(len(st))
