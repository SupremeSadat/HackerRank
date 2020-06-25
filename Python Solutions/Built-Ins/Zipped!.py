a,b = input().split()
c = list(zip(*list([input().split() for x in range(int(b))])))
for x in c:
    print(sum(list(map(float, (x))))/len(x))
