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


def solution(products):
    N, P = len(products), len(products[0])
    for line in products:
        line.sort()
    @functools.lru_cache(None)
    def sub(i, j):
        if i == 0:
            if j == 0:
                return products[0][-1] + abs(products[0][-1] - products[0][0])
            else:
                return products[0][-1]
        if j == 0:
            # previous min -> cur max -> cur min
            cand0 = sub(i-1,0) + abs(products[i-1][0] - products[i][-1]) + abs(products[i][-1] - products[i][0])
            # previous max -> cur max -> cur min
            cand1 = sub(i-1,1) + abs(products[i-1][-1] - products[i][-1]) + abs(products[i][-1] - products[i][0])
        else:
            # previous min -> cur min -> cur max
            cand0 = sub(i-1,0) + abs(products[i-1][0] - products[i][0]) + abs(products[i][-1] - products[i][0])
            # previous max -> cur min -> cur max
            cand1 = sub(i-1,1) + abs(products[i-1][-1] - products[i][0]) + abs(products[i][-1] - products[i][0])
        ans = min(cand0, cand1)
        return ans
    ans = min(sub(N-1, 0), sub(N-1,1))
    return ans

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    N, P = map(int, input().split())
    products = []
    for _ in range(N):
        products.append(list(map(int, input().split())))
    res = solution(products)
    print("Case #{}: {}".format(case_num, res))
