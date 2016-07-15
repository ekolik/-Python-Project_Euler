## see https://www.alpertron.com.ar/QUAD.HTM

b = 15
n = 21
limit = 10**12

while n < limit:
    cur_n = 4*b+3*n-3
    cur_b = 3*b+2*n-2

    n = cur_n
    b = cur_b

print(cur_b)
