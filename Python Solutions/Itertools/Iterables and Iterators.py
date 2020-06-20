import itertools
input()
a = list(input().split())
c = int(input())
b = list(itertools.combinations(a,c))
print(sum('a' in item for item in b)/len(b))
