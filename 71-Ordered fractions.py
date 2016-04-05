limit = 1000000
loc_a = 0
loc_b = 1
low_bound = 0
b = limit

while b > low_bound:
    # see https://en.wikipedia.org/wiki/Farey_sequence#Farey_neighbours
    if (3*b-1) % 7 == 0:
        a = int((3*b-1)/7)
        if loc_a * b < loc_b * a:
            loc_a = a
            loc_b = b
            low_bound = loc_b / (3*loc_b - 7*loc_a)
    b -= 1

print(loc_a)