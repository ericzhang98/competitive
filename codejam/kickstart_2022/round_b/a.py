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

def solution(R, A, B):
    ans = 0
    cur = R
    while cur > 0:
        ans += cur**2
        cur = cur * A
        ans += cur**2
        cur = cur // B
    return ans * math.pi

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    R, A, B = map(int, input().split())
    res = solution(R, A, B)
    print("Case #{}: {}".format(case_num, res))
