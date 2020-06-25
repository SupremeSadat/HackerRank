cube = lambda x:  x**3

def fibonacci(n):
    if n ==0:
        return []
    if n ==1:
        return [0]
    if n ==2:
        return[0,1]
    arr = [0,1]
    x1 = 0
    x2 = 1
    while len(arr) <= n-1:
        x3 = x1 + x2
        arr.append(x3)
        x1 = x2
        x2 = x3
    return arr

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))