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

def dist(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

"""
def check(kids, sweets, all_distances, sweet_ordering_for_kid):
    blueberry = 0
    sweets_left = set(sweets)
    def dfs(i):
        # eprint("hi", i, sweets, len(kids))
        if i == len(kids):
            return list(sweets_left)[0] == blueberry, []
        kid = kids[i]
        # eprint("dists", sweets_dist)
        sweet_cands = []
        first_valid = None
        sweet_ordering = sweet_ordering_for_kid[kid]
        # eprint(kid, sweet_ordering)
        for sweet_cand in sweet_ordering:
            if sweet_cand in sweets_left:
                if first_valid is None:
                    first_valid = sweet_cand
                    sweet_cands.append(sweet_cand)
                else:
                    if abs(all_distances[kid][first_valid] - all_distances[kid][sweet_cand]) < 1e-6:
                        sweet_cands.append(sweet_cand)
        # eprint(sweet_cands)
        for sweet in sweet_cands:
            sweets_left.remove(sweet)
            good, stack = dfs(i+1)
            if good:
                return True, [sweet] + stack
            sweets_left.add(sweet)
        return False, []
    good, ans = dfs(0)
    if good:
        return True, ans
    else:
        return False, None
"""

"""
def check(kids, sweets, sweet_ordering_for_kid):
    blueberry = 0
    sweets_left = set(sweets)
    ans = []
    for kid in kids:
        sweet_ordering = sweet_ordering_for_kid[kid]
        for sweet in sweet_ordering:
            if sweet in sweets_left:
                if sweet == blueberry:
                    return False, []
                ans.append(sweet)
                sweets_left.remove(sweet)
                break
    assert(len(sweets_left) == 1)
    if list(sweets_left)[0] == blueberry:
        return True, ans
    else:
        return False, []
"""

def dfs(N, sweet_ordering_for_kid, kids_left, sweets_left, ans):
    blueberry = 0
    if len(kids_left) == 0:
        assert len(sweets_left) == 1
        if list(sweets_left)[0] == blueberry:
            return ans
        else:
            return None
    for kid in range(N):
        if kid in kids_left:
            kids_left.remove(kid)
            sweet_ordering = sweet_ordering_for_kid[kid]
            next_sweet = None
            for sweet in sweet_ordering:
                if sweet in sweets_left:
                    next_sweet = sweet
                    break
            if next_sweet != blueberry:
                sweets_left.remove(next_sweet)
                res = dfs(N, sweet_ordering_for_kid, kids_left, sweets_left, ans + [(kid,next_sweet)])
                if res is not None:
                    return res
                sweets_left.add(next_sweet)
            else:
                kids_left.add(kid)
                continue

            kids_left.add(kid)
    return None


def solution(kids, sweets):
    N = len(kids)
    all_distances = [[0]*(N+1) for _ in range(N)]
    for i, kid in enumerate(kids):
        for j, sweet in enumerate(sweets):
            all_distances[i][j] = dist(kid[0], kid[1], sweet[0], sweet[1])
    # sweet_ordering_for_kid = [list(sorted(list(range(N+1)), key=lambda sweet: all_distances[kid][sweet])) for kid in range(N)]
    sweet_ordering_for_kid = []
    for kid in range(N):
        sweet_ordering = list(sorted(range(1,N+1), key=lambda sweet: all_distances[kid][sweet]))
        for i in range(len(sweet_ordering)):
            if all_distances[kid][0] < all_distances[kid][sweet_ordering[i]] - 1e-6:
                sweet_ordering.insert(i, 0)
                break
        else:
            sweet_ordering.append(0)
        sweet_ordering_for_kid.append(sweet_ordering)
    # eprint(sweet_ordering_for_kid)
    kids = list(range(N))
    sweets = list(range(N+1))
    # for perm in itertools.permutations(kids):
    #     # eprint(perm)
    #     # good, sweets_ordering = check(perm, sweets, all_distances, sweet_ordering_for_kid)
    #     good, sweets_ordering = check(perm, sweets, sweet_ordering_for_kid)
    #     if good:
    #         s = []
    #         for a,b in zip(perm, sweets_ordering):
    #             s.append(f"{a+1} {b+1}")
    #         s = "\n".join(s)
    #         return f"POSSIBLE \n{s}"
    ans = dfs(N, sweet_ordering_for_kid, set(range(N)), set(range(N+1)), [])
    if ans is not None:
        s = []
        for a,b in ans:
            s.append(f"{a+1} {b+1}")
        s = "\n".join(s)
        return f"POSSIBLE \n{s}"

    return "IMPOSSIBLE"

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    N = int(input())
    kids = []
    sweets = []
    for _ in range(N):
        kids.append(list(map(int, input().split())))
    for _ in range(N+1):
        sweets.append(list(map(int, input().split())))
    res = solution(kids, sweets)
    print("Case #{}: {}".format(case_num, res))
