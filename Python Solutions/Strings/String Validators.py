if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    low = False
    up = False

    for x in s:
        if x.isalnum() == True:
            alnum = True
        if x.isalpha() == True:
            alpha = True
        if x.isdigit() == True:
            digit = True
        if x.islower() == True:
            low = True
        if x.isupper() == True:
            up = True
    print(alnum)
    print(alpha)
    print(digit)
    print(low)
    print(up)