from __future__ import print_function
input = raw_input
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

def solution(R, B):
    return dp[R][B]

MAX_R, MAX_B = 50, 50
dp = [[0 for _ in range(MAX_B+1)] for _ in range(MAX_R+1)]
for i in range(MAX_R+1):
    if i*(i+1)//2 > MAX_R:
        break
    for j in range(MAX_B+1):
        if j*(j+1)//2 > MAX_B:
            break
        if (i, j) == (0, 0):
            continue
        if (j+1)*i*(i+1)//2 > MAX_R or (i+1)*j*(j+1)//2 > MAX_B:
            break
        for r in reversed(range(i, MAX_R+1)):
               for b in reversed(range(j, MAX_B+1)):
                   dp[r][b] = max(dp[r][b], 1+dp[r-i][b-j])

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    R, B = list(map(int, input().split(" ")))
    res = solution(R, B)
    print("Case #{}: {}".format(case_num, res))
