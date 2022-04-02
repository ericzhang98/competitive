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

def solution(s):
    highlight = set()
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] < s[j]:
                highlight.add(i)
                break
            if s[i] > s[j]:
                break
    res = []
    for i, c in enumerate(list(s)):
        res.append(c)
        if i in highlight:
            res.append(c)
    return "".join(res)

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    s = input()
    res = solution(s)
    print("Case #{}: {}".format(case_num, res))
