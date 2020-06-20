import collections

d = collections.defaultdict(list)
a, b = input().split()
for x in range(1, int(a) + 1):
    d[x].append(input())
for x in range(int(b)):
    c = input()
    for key, value in d.items():
        if value == [c]:
            print(key, end=' ')

    if [c] not in d.values():
        print(-1, end=' ')
    print()