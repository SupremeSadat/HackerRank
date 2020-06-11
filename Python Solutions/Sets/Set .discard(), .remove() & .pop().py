n = int(input())
s = set(map(int, input().split()))
z = int(input())
for x in range(z):
    y = input().split()
    if y[0] == 'remove':
        s.remove(int(y[1]))
    if y[0] == 'pop':
        s.pop()
    if y[0] == 'discard':
        s.discard(int(y[1]))
print(sum(s))
