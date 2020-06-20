import itertools
x = input()
x = itertools.groupby(x)
print(*[(len(list(item)), int(key)) for key,item in x])

