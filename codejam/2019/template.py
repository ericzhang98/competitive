from __future__ import print_function
import sys
import math
from collections import defaultdict

def solution(args):
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
    params.append(line)

    res = solution(params)
    print("Case #{}: {}".format(case_num, res))
