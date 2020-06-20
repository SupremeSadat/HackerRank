import collections
a = int(input())
mark = collections.namedtuple('mark', input().split())
print(sum(int(mark._make(input().split()).MARKS) for x in range(a))/a)