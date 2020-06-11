N = int(input())
for n in range(N):
    input()
    A = set(input().split())
    input()
    B = set(input().split())
    print(A==B.intersection(A))