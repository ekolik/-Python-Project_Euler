import math
limit = math.factorial(9)*3 + math.factorial(8)*3 + math.factorial(1)
final = 0

### to speed up the factorial calculations by pre-calculating and storing the results
factorials = []
for i in range(0, 10):
    factorials.append(math.factorial(i))
#print(factorials)

for i in range(10, limit):
    sum = 0
    for letter in (str(i)):
        sum += factorials[int(letter)]
    if i == sum:
        final += i
        #print(i)

print(final)