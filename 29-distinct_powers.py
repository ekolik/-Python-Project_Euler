# limit = 100
# st = set()
# for a in range(2, limit+1):
#     for b in range(2, limit+1):
#         st |= {pow(a,b)}
# print(len(st))


#
# _____________OR__________________
print(len(set([a**b for a in range(2,101) for b in range(2,101)])))