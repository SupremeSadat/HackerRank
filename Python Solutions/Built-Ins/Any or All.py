n,N = input(),input().split()
print(all(x>0 for x in map(int,N)) and any(list(y)==list(reversed(y)) for y in N))
