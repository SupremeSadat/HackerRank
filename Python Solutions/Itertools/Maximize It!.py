import itertools
a = list(map(int,input().split()))
b = []
for x in range(a[0]):
    d = input().split()
    b.append(list(map(int, d[1:])))
c = list(itertools.product(*b))
final =0
for x in c:
    current = sum(item**2 for item in x)%a[1]
    if current> final:
        final = current
print(final)
