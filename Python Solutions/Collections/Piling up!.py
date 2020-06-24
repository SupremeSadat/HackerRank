import collections
for x in range(int(input())):
    input()
    d = collections.deque()
    d.extend(list(map(int,input().split())))
    #print(d)
    for box in reversed(sorted(d)):
        if box == d[0]:
            d.popleft()
        elif box == d[-1]:
            d.pop()
        else:
            print('No')
            break
    if len(d)==0:
        print('Yes')
