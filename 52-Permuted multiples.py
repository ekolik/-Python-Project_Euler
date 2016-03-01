start = 10
end = 16
while True:
    for x in range(start, end+1):
        if all(sorted(str(x)) == sorted(str(i*x)) for i in range(2, 7)):
            print(x)
            break
    else:
        start *= 10
        end = end*10+6
        #print(start)
        continue
    break
