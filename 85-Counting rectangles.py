err = 10**6
area = 0
tgt = 2000000

n_init = 2000
m_init = 1

while n_init >= m_init:
    rects = n_init*(n_init+1)*m_init*(m_init+1)/4
    if err > abs(rects-tgt):
        area = n_init * m_init
        err = abs(rects - tgt)
        ans_n = n_init
        ans_m = m_init
    if rects > tgt:
        n_init -= 1
    else:
        m_init += 1

print(area, ans_n, ans_m)