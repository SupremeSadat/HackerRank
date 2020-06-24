import collections
d = collections.OrderedDict()
for x in range(int(input())):
    a = input()
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
print(len(d.items()))
print(*d.values())