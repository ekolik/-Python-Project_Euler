with open("13-input") as f:
    content = f.readlines()

for i in range(len(content)):
    content[i] = int(content[i][:13])

print(str(sum(content))[:10])

