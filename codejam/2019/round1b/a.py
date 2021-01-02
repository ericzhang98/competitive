from __future__ import print_function
import sys
import math
from collections import defaultdict

def solution(args):
    p = args[0]
    q = args[1]
    arr = args[2]
    north = matrix(q+1,q+1,int)
    east = matrix(q+1,q+1,int)
    south = matrix(q+1,q+1,int)
    west = matrix(q+1,q+1,int)


    return 0

def matrix(height, width, type=int):
    return [[type() for _ in range(w)] for _ in range(h)]

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

t = int(raw_input()) # read a line with a single integer
for case_num in xrange(1, t + 1):

    params = []

    # parsing
    line = raw_input()
    arr = line.split()
    p = int(arr[0])
    q = int(arr[1])
    params.append(p)
    params.append(q)
    arr = []
    for i in range(p):
        line = raw_input()
        arr.append(line)
    params.append(arr)

    res = solution(params)
    print("Case #{}: {}".format(case_num, res))
