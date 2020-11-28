from __future__ import print_function
import sys
import math

def solution(args):
    num = int(args[0])
    a = 0
    b = num

    while has_four(a) or has_four(b):
        a += 1
        b -= 1

    return "%d %d" % (a,b)

def has_four(num):
    return '4' in str(num)

def matrix(height, width, type=int):
    return [[type() for _ in range(w)] for _ in range(h)]

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

t = int(raw_input()) # read a line with a single integer
for case_num in xrange(1, t + 1):
    line = raw_input()

    params = line.split(" ")

    res = solution(params)
    print("Case #{}: {}".format(case_num, res))
