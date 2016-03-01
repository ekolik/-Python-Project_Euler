import math
digit = 1000
n = (digit-1 + math.log10(5)/2)/math.log10((1+math.sqrt(5))/2)
print(math.ceil(n))