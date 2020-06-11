input()
A = set(map(int,list(input().split())))
input()
B = set(map(int, list(input().split())))
array = sorted(list(A.difference(B)) + list(B.difference(A)))
print(*array,sep = "\n")

