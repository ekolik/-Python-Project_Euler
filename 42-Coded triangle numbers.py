content = open("42-input.txt").read()
content = content.replace('"', '')
words = content.split(',')

values = []
for word in words:
    values.append(0)
    for letter in word.lower():
        values[-1] += ord(letter)-ord('a')+1


def tria_nums(max_n):
    nums = []
    i = 1
    while int(i*(i+1)/2) <= max_n:
        nums.append(int(i*(i+1)/2))
        i += 1
    return nums

all_tria_nums = tria_nums(max(values))
res = 0
for value in values:
    if value in all_tria_nums:
        res += 1

print(res)