limit = 10000


def reverse(num):
    return int(str(num)[::-1])


def is_palin(num):
    return num == reverse(num) and len(str(num)) == len(str(reverse(num)))

# cache[] == 0 => haven't checked yet
# cache[] == 1 => checked: produces palindrome
# cache[] == 2 => checked: lychrel number

cache = [0]*limit
count = 0

for num in range(limit):
    if cache[num] == 0:
        local = []
        sum = num
        for i in range(50):
            if sum < limit:
                local.append(sum)
            if reverse(sum) < limit:
                local.append(reverse(sum))
            sum += reverse(sum)
            if is_palin(sum):
                for j in local:
                    cache[j] = 1
                break
        else:
            cache[num] = cache[reverse(num)] = 2
            count += 1
    elif cache[num] == 2:
        count += 1

print(count)
