limit = 10000


def cf(n1, n2, d, res):
    # implementation of the algorithm from http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html#section6.2.2
    m = int((int(n1**0.5) + n2)/d)
    res.append(m)
    if m**2 == n1:
        return res

    x_n1 = n1
    x_n2 = abs(n2 - m*d)
    x_d = int((n1 - x_n2**2)/d)

    if x_d == 1 and x_n2 == res[0]:
        res.append(res[0]*2)
        return res

    cf(x_n1, x_n2, x_d, res)
    return res


count = 0
for n in range(limit):
    frac = cf(n, 0, 1, [])
    #print(frac)
    if len(frac) > 1 and len(frac)%2 == 0:
        count += 1
print(count)