import itertools
x = input().split()
print(*["".join(i) for i in list(itertools.combinations_with_replacement(sorted(x[0]), int(x[1])))], sep='\n')
