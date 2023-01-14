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

sys.setrecursionlimit(100)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution(n, d, v):
    @functools.lru_cache(None)
    def dp(i, j, target):
        while i < n and v[i] == target:
            i+= 1
        while j >= 0 and v[j] == target:
            j -= 1
        if j < i:
            return 0
        diffi = min((v[i] - target) % d, (target - v[i]) % d)
        diffj = min((v[j] - target) % d, (target - v[j]) % d)
        cand1 = diffi + dp(i+1, j, v[i])
        cand2 = diffj + dp(i, j-1, v[j])
        best = min(cand1, cand2)
        return best
    ans = dp(0, n-1, 0)
    return ans

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    N, D = map(int, input().split())
    V = list(map(int, input().split()))
    res = solution(N, D, V)
    print("Case #{}: {}".format(case_num, res))
