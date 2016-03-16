limit = 1000
dct = {}


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


for n in range(limit):
    # using https://en.wikipedia.org/wiki/Pell's_equation#Fundamental_solution_via_continued_fractions
    frac = cf(n, 0, 1, [])
    if len(frac) == 1:
        continue
    num_1, num_2 = 1, frac[0]
    den_1, den_2 = 0, 1
    while True:
        for i in range(1,len(frac)):
            num_1, num_2 = num_2, num_2*frac[i]+num_1
            den_1, den_2 = den_2, den_2*frac[i]+den_1
            if (num_2**2) - n*(den_2**2) == 1:
                dct[n] = num_2
                break
        else:
            continue
        break

print(max(dct, key=dct.get))
