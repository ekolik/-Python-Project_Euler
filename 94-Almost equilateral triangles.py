limit = 1000000000
res = 0
x = 2
y = 1
side = 0

while True:
    # bottom = side + 1
    side = (2*x - 1)/3
    if side*3 >= limit:
        break
    area = (x-2)*y/3
    if area > 0 and side == int(side) and area == int(area):
        res += (3*int(side) + 1)

    # bottom = side - 1
    side = (2*x + 1)/3
    area = (x+2)*y/3
    if side == int(side) and area == int(area):
        res += (3*int(side) - 1)

    nextx = 2*x + 3*y
    nexty = 2*y + x
    x = nextx
    y = nexty

print(res)
