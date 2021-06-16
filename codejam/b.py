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

def solution(N):
    # dp on (sides left, current outer polygon size), by fitting next outer polygon
    # ans is best among all possible starting polygon sizes
    @functools.lru_cache(None)
    def solve(sides_left, polygon_size):
        #eprint(sides_left, polygon_size)
        sides_left -= polygon_size
        if sides_left == 0:
            return 1
        if sides_left < 3:
            return float('-inf')
        # can only choose an outer polygon that is multiple of current outer polygon size and outer polygon divides sides left
        best = float('-inf')
        for nxt_polygon_size in range(polygon_size * 2, sides_left+1, polygon_size):
            if sides_left % nxt_polygon_size == 0:
                best = max(best, solve(sides_left, nxt_polygon_size))
        return 1 + best

    cands = []
    for divisor in range(1, math.ceil(N**0.5) + 1):
        if N % divisor == 0:
            if divisor > 2:
                cands.append(divisor)
            if N // divisor > 2:
                cands.append(N // divisor)
    #eprint(cands)
    ans = max(solve(N, initial_polygon_size) for initial_polygon_size in cands)
    return ans



def solution_better(N):
    # dp on (sides left, current outer polygon size), by fitting next outer polygon
    # ans is best among all possible starting polygon sizes
    # f(sides left, current outer polygon size) == f(sides left / current outer polygon size, 1)
    @functools.lru_cache(None)
    def solve_better(sides_left, polygon_size):
        sides_left -= polygon_size
        if sides_left == 0:
            return 1
        if sides_left < 0:
            return float('-inf')
        # can only choose an outer polygon that is multiple of current outer polygon size and outer polygon divides sides left
        best = float('-inf')
        for nxt_polygon_size in range(polygon_size * 2, sides_left+1, polygon_size):
            if sides_left % nxt_polygon_size == 0:
                best = max(best, solve_better(sides_left // nxt_polygon_size, 1))
        return 1 + best
    cands = []
    for divisor in range(1, math.ceil(N**0.5) + 1):
        if N % divisor == 0:
            if divisor > 2:
                cands.append(divisor)
            if N // divisor > 2:
                cands.append(N // divisor)
    ans = max(solve_better(N, initial_polygon_size) for initial_polygon_size in cands)
    return ans

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    N = int(input())
    res = solution_better(N)
    print("Case #{}: {}".format(case_num, res))
