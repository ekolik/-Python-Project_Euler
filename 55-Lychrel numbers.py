limit = 10000


def reverse(num):
    return int(str(num)[::-1])


# palins[] == 0 => haven't checked yet
# palins[] == 1 => checked: produces palindrome
# palins[] == 2 => checked: lychrel number

palins = [0]*limit
count = 0

for num in range(limit):
    if palins[num] == 0:
        local = []
        sum = num
        for i in range(50):
            if sum < limit:
                local.append(sum)
            if reverse(sum) < limit:
                local.append(reverse(sum))
            sum += reverse(sum)
            if sum == reverse(sum):
                for j in local:
                    palins[j] = 1
                break
        else:
            palins[num] = palins[reverse(num)] = 2
            count += 1
    elif palins[num] == 2:
        count += 1

print(count)