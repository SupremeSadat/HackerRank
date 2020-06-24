#!/bin/python3

import math
import os
import random
import re
import sys
import collections


if __name__ == '__main__':
    d = collections.OrderedDict()
    s = input()
    for x in s:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    d = collections.OrderedDict(sorted(d.items(), key=lambda x:x[1], reverse=True))
    print(d)
    i = 0
    for x in d:
        i=i+1
        if d[x]!=1:
            print(x, d[x])
        if i ==3:
            break