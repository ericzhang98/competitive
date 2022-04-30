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

def solution(nums):
    dq = collections.deque(nums)
    ans = 0
    cur = float('-inf')
    while dq:
        if dq[0] <= dq[-1]:
            cand = dq.popleft()
        else:
            cand = dq.pop()
        if cand >= cur:
            ans += 1
            cur = cand
    return ans

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    N = input()
    nums = map(int,input().split())
    res = solution(nums)
    print("Case #{}: {}".format(case_num, res))
