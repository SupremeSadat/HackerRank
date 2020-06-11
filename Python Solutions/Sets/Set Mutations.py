input()
s = set(input().split())
N = int(input())
for x in range(N):
    y = input().split()
    if y[0] == 'intersection_update':
        s.intersection_update(input().split())
    if y[0] == 'update':
        s.update(input().split())
    if y[0] == 'symmetric_difference_update':
        s.symmetric_difference_update(input().split())
    if y[0] == 'difference_update':
        s.difference_update(input().split())
print(sum(map(int, s)))
