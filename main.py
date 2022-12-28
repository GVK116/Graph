from math import *
from functools import reduce


def xorSequence(l, r):
    a = [0]
    [a.append(a[-1]^i) for i in range(1,r+1)]
    return reduce(lambda x,y:x^y,a[l:] ),a


for _ in range(int(input())):
    print(xorSequence(int(input()),int(input())))