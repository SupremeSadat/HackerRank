a = set(input().split())
start = True
for x in range(int(input())):
    b = set(input().split())

    if b == a.intersection(b) and a != b:
        start = True
    else:
        start = False
        break
print(start)
