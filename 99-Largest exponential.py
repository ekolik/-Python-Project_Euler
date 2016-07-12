from math import log

file = open("99-input.txt").readlines()

mx = 0
mx_line = 0
for count, line in enumerate(file, start=1):
    base, expon = map(int, line.split(','))
    cur = log(base)*expon
    if cur > mx:
        mx = cur
        mx_line = count

print(mx_line)


