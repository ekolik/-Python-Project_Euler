from fractions import gcd
limit = 1500000
mlimit = int((limit/2)**0.5)
counts = [0]*limit

for m in range(2, mlimit):
    for n in range(1, m):
        if (m-n) % 2 == 1 and gcd(m,n) == 1:
            p = m**2-n**2 + 2*m*n + m**2+n**2
            for shift in range(p, limit, p):
                counts[shift] += 1

print(counts.count(1))
