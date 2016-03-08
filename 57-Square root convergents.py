def digits(num):
    return len(str(num))


def expansion(n):
    if n == 8:
        return [1393, 985, 1]
    else:
        prev = expansion(n-1)
        curr = [2*prev[1] + prev[0], prev[1] + prev[0], prev[2]]

        if digits(curr[0]) > digits(curr[1]):
            curr[2] += 1
        return curr

print(expansion(999)[2])