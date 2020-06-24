import collections
d = collections.deque()
for x in range(int(input())):
    a = input().split()
    if a[0] == 'append':
        d.append(int(a[1]))
    elif a[0] == 'appendleft':
        d.appendleft(int(a[1]))
    elif a[0] == 'pop':
        d.pop()
    elif a[0] == 'popleft':
        d.popleft()
print(*d)