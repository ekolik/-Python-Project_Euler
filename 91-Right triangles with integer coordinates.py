from fractions import gcd
size = 50
res = 0

for x in range(1, size):
    for y in range(1, size+1):
        cur_gcd = gcd(x, y)
        res += min((size-x)*cur_gcd//y, y*cur_gcd//x)

print(res*2 + size**2 *3)