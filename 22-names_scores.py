import re
with open("22-input.txt") as f:
    content = f.readlines()

names = list()

for i in range(len(content)):
    curr = content[i].strip().split(',')
    for name in curr:
        name = re.sub(r'\"', '', name)
        names.append(name)

count = 0
final = 0
for name in sorted(names):
    count += 1

    score = 0
    for letter in name.lower():
        score += (ord(letter)-ord('a')+1)

    final += count*score

print(final)