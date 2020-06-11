def swap_case(s):
    p = ""
    for _ in s:
        if _.isupper():
            p +=_.lower()
        elif _.islower():
            p+=_.upper()
        else:
            p+=_
    return p

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# Can also do with swapcase function in string module
# import string
# def swap_case(s):
#     return s.swapcase()
#
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)