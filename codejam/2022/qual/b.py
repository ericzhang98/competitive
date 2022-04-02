import sys
import copy
import operator
import math
import collections
import heapq
import itertools
import functools
import bisect

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution(c1,c2,c3):
    a = min(c1[0], c2[0], c3[0])
    b = min(c1[1], c2[1], c3[1])
    c = min(c1[2], c2[2], c3[2])
    d = min(c1[3], c2[3], c3[3])
    if a+b+c+d < 10**6:
        return "IMPOSSIBLE"
    remaining = 10**6
    res = []
    for x in [a,b,c,d]:
        y = min(x, remaining)
        res.append(y)
        remaining -= y
    return " ".join(map(str, res))

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    c1 = list(map(int,input().split()))
    c2 = list(map(int,input().split()))
    c3 = list(map(int,input().split()))
    res = solution(c1,c2,c3)
    print("Case #{}: {}".format(case_num, res))
