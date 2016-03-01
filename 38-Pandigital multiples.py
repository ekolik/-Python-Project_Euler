for num in range(9876, 9124, -1):
    stri = str(num) + str(2*num)

    if ''.join(sorted(stri)) == '123456789':
        print(stri)
        break