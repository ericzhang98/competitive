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

def solution(X):
    S = list(str(X))
    N = len(S)
    digit = -X % 9
    for idx in range(N):
        if digit == 0 and idx == 0:
            continue
        nxt_digit = int(S[idx])
        # cap is lt nxt_digit
        if digit < nxt_digit:
            return "".join(S[:idx]) + str(digit) + "".join(S[idx:])
    return str(X) + str(digit)

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    N = int(input())
    res = solution(N)
    print("Case #{}: {}".format(case_num, res))
