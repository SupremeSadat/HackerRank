N = int(input())
s = input().split()
s = list(map(int, s))
x = set()
y = set()

for z in s:

    if z in x:
        y.add(z)
    else:
        x.add(z)
print(sum(x) - sum(y))
