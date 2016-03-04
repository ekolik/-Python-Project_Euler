from collections import Counter

with open("54-input.txt") as f:
    content = f.readlines()


all_values = {r: i for i, r in enumerate('23456789TJQKA', start=2)}
straights = [[v, v-1, v-2, v-3, v-4] for v in range(14, 5, -1)]


def h_value(hand):
    value = []
    for i in range(0, len(hand), 2):
        value.append(all_values[hand[i]])
    value = sorted(value, reverse=True)
    return value


def max_suit(hand):
    suits = []
    for i in range(1, len(hand)+1, 2):
        suits.append(i)
    c = Counter(suits)
    return max(c.values())


def rank(hand):
    value = h_value(hand)
    c = Counter(value)

    if max_suit(hand) == 5 and value == [14, 13, 12, 11, 10]:
        return [10]

    if max_suit(hand) == 5 and value in straights:
        return [9]

    if max(c.values()) == 4:
        return [8]

    if max_suit(hand) >= 3 and max(c.values()) >= 2:
        return [7, sorted(c.most_common(), reverse=True)[0][0]]

    if max_suit(hand) == 5:
        return [6] + value

    if value in straights:
        return [5] + value

    if max(c.values()) == 3:
        return [4, c.most_common()[0][0]]

    if sorted(c.values()) == [1, 2, 2]:
        return [3, max(c.most_common()[0][0], c.most_common()[1][0]), min(c.most_common()[0][0], c.most_common()[1][0])]

    if max(c.values()) == 2:
        return [2, c.most_common()[0][0]] + value

    return [1] + value


count = 0
for i in range(len(content)):
    curr = content[i].strip().split(' ')
    first = ''.join(curr[:5])
    second = ''.join(curr[5:])

    if rank(first) > rank(second):
        count += 1
    elif rank(first) == rank(second):
        print('tie! debug, please')


print(count)