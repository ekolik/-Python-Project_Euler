total = 11
sum = 0


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num%2 == 0 or num%3 == 0:
        return False
    i = 5
    while i*i <= num:
        if num%i == 0 or num%(i+2) == 0:
            return False
        i += 6
    return True


def left(num):
    str_n = str(num)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True


def right(num):
    str_n = str(num)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[:i])):
            return False
    return True


num = 11
while total:
    if is_prime(num):
        if left(num):
            if right(num):
                total -= 1
                sum += num
                print(num)
    num += 2

print(sum)