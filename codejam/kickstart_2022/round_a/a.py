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

def solution(A, B):
    p1, p2 = 0, 0
    ans = 0
    while p2 < len(B):
        if p1 < len(A) and B[p2] == A[p1]:
            p1 += 1
        else:
            ans += 1
        p2 += 1
    if p1 != len(A):
        return "IMPOSSIBLE"
    return ans

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    I = input()
    P = input()
    res = solution(I, P)
    print("Case #{}: {}".format(case_num, res))
