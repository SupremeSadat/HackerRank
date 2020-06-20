from collections import OrderedDict

ordered_dictionary = OrderedDict()
for x in range(int(input())):
    a, c, b = input().rpartition(' ')

    if a in ordered_dictionary:
        ordered_dictionary[a] += int(b)
    else:
        ordered_dictionary[a] = int(b)
for key, value in ordered_dictionary.items():
    print(key, value)