d31 = [1, 3, 5, 7, 8, 10, 12]
d30 = [4, 6, 9, 11]
sunday = 7
count = 0

for year in range(1900, 2001):
    for month in range(1,13):
        if month == 12 and year == 2000:
            break

        sunday += 4*7

        if month in d31:
            if sunday <= 31:
                sunday += 7
            sunday -= 31
        elif month in d30:
            if sunday <= 30:
                sunday += 7
            sunday -= 30
        elif year%400 != 0 or (year%100 != 0 and year%4 == 0):
            if sunday <= 29:
                sunday += 7
            sunday -= 29
        else:
            sunday -= 28

        if year >= 1901:
            if sunday == 1:
                count += 1

print(count)