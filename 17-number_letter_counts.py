units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
elevens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
dozens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
units_c = []
dozens_c = []
elevens_c = []
hundred_c = 7

for i in units:
    units_c.append(len(i))
for i in dozens:
    dozens_c.append(len(i))
for i in elevens:
    elevens_c.append(len(i))

oneto99 = sum(elevens_c) + sum(dozens_c)*10 + sum(units_c)*9

hunto1000 = 9 * (oneto99 + (99+1)*hundred_c + 99*len('and')) + (99+1)*sum(units_c) + len('one') + len('thousand')
print(hunto1000+oneto99)