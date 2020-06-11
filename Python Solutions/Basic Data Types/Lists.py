if __name__ == '__main__':
    N = int(input())
    storage = []
    for _ in range(N):
        prompt = input()
        key = prompt.split()

        if key[0] == 'insert':
            storage.insert(int(key[1]), int(key[2]))
        elif key[0] == 'print':
            print(storage)
        elif key[0] == 'remove':
            storage.remove(int(key[1]))
        elif key[0] == 'append':
            storage.append(int(key[1]))
        elif key[0] == 'sort':
            storage.sort()
        elif key[0] == 'pop':
            storage.pop()
        elif key[0] == 'reverse':
            storage.reverse()