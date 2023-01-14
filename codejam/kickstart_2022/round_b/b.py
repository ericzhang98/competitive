import sys
import copy
import operator
import math
import collections
import heapq
import itertools
import functools
import bisect
import random

sys.setrecursionlimit(1000000000)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution(x):
    cnt = 0
    for factor in range(1, int(math.sqrt(x)) + 1):
        if x % factor == 0:
            if str(factor) == str(factor)[::-1]:
                cnt += 1
            factor2 = x // factor
            if factor != factor2 and str(factor2) == str(factor2)[::-1]:
                cnt += 1
    return cnt

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    x = int(input())
    res = solution(x)
    print("Case #{}: {}".format(case_num, res))
