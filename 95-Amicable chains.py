limit = 1000000

div_sum = [1] * limit
for i in range(2, limit//2):
    for j in range(2*i, limit, i):
        div_sum[j] += i


max_chain_length = 0
for i in range(2, limit):
    chain = []
    next = i
    while next < limit:
        if next not in chain:
            chain.append(next)
        else:
            corr_chain = chain[chain.index(next):]
            if len(corr_chain) > max_chain_length:
                max_chain_length = len(corr_chain)
                min_elem = min(corr_chain)
            break

        next = div_sum[next]

print(min_elem)