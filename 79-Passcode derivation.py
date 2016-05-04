atts = set(str(l.strip()) for l in open("79-input.txt").readlines())
#print(len(atts))
#print(sorted(atts))

d = dict()
for att in atts:
    if att[0] in d.keys():
        d[att[0]] |= {att[1]}
    else:
        d[att[0]] = {att[1]}
    if att[1] in d.keys():
        d[att[1]] |= {att[2]}
    else:
        d[att[1]] = {att[2]}

for item in d.items():
    print(item)