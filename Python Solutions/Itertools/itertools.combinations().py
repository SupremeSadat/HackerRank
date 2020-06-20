import itertools
x = input().split()
for y in range(1, int(x[1])+1):
    print(*["".join(i) for i in list(itertools.combinations(sorted(x[0]), y))], sep='\n')
