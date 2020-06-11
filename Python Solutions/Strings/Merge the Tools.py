def merge_the_tools(string, k):
    mylist = list(string)
    for i in range(0, int(len(string)),k):
        temp = list(dict.fromkeys(mylist[i:i+k]))
        print(*temp, sep = "")
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    