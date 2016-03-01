limit = 1000000
sum = 0


### brute force approach - works nice
# for i in range(1, limit, 2):
#     if str(i) == str(i)[::-1]:
#         b = bin(i)
#         if b.strip('0b') == b[::-1].strip('0b'):
#             sum += i
# print(sum)


### smarter approach
# Suppose we have a palindrome of the form xyzzyx in base b, then the first 3 digits define the
# palindrome. However, the 3 digits xyz also define the palindrome xyzyx. So the 3-digit number
# xyz defines a 5-digit palindrome and a 6 digit palindrome. From which follows that every
# positive number less than b^n generates two palindromes less than b^2n .


def makepalin(n, oddness):
    res = n
    if oddness:
        n //= 10
    while n > 0:
        res = res*10 + n%10
        n //= 10
    return res


n = 1
p = makepalin(n, 1)
while p < limit:
        b = bin(p)
        if b.lstrip('0b') == b[::-1].rstrip('0b'):
            sum += p
        n += 1
        p = makepalin(n, 1)

n = 1
p = makepalin(n, 0)
while p < limit:
        b = bin(p)
        if b.lstrip('0b') == b[::-1].rstrip('0b'):
            sum += p
        n += 1
        p = makepalin(n, 0)
print(sum)