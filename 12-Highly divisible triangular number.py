def prime_factors(num):
    factors = []
    d = 2
    while num > 1:
        while num % d == 0:
            factors.append(d)
            num /= d
        d += 1
        if d * d > num:
            if num > 1: factors.append(num)
            break
    # print factors

    return factors

n = rawn = raw_input()
n = int(n)

numbers = [int(raw_input()) for i in range(n)]
answers = []
a = s = 1
#print max(numbers)
for i in range(max(numbers)+1):

	    # a = numbers[i]
	    # s = int((1+a)*a/2)

    while a:
        factors_s = prime_factors(s)
        divisors = 1
        g = 1
        for k in range(len(factors_s)):
            if k < (len(factors_s) - 1) and factors_s[k] == factors_s[k + 1]:
                g += 1
            else:
                divisors *= (g + 1)
                g = 1
        if divisors > i:
            answers.append(s)
            break
        a += 1
        s += a
#print answers

for j in range(n):
    print answers[numbers[j]]
