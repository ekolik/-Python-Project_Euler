from itertools import cycle, product

content = list(map(int, open("59-input.txt").read().split(',')))

for poss_key in product(range(97, 123), repeat=3):
    result = [x ^ y for x, y in zip(content, cycle(poss_key))]
    if ' the ' in ''.join(chr(i) for i in result):
        print(''.join(chr(i) for i in result))
        print(poss_key)
        print(sum(result))
        break
