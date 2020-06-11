if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

arr.sort(reverse = True)
first = arr[0]
second = first
i = 0
while second == first:
    second = arr[i]
    i = i + 1

print(second)