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

def brute_force_solution(weights):
    E, W = len(weights), len(weights[0])
    visited = {}
    q = collections.deque([((0, tuple()), 0)])
    while q:
        (cur_e, cur_stack), dist = q.popleft()
        if (cur_e, cur_stack) in visited:
            continue
        visited[(cur_e, cur_stack)] = dist
        if cur_e == E:
            visited[(cur_e, tuple())] = dist + len(cur_stack)
            break
        cur_stack_cnt = [0]*W
        for w in cur_stack:
            cur_stack_cnt[w] += 1
        if cur_stack_cnt == weights[cur_e]:
            q.append(((cur_e+1, cur_stack), dist))
        if len(cur_stack) >= 1:
            q.append(((cur_e, cur_stack[:-1]), dist+1))
        append_cands = []
        for i in range(W):
            if cur_stack_cnt[i] < weights[cur_e][i]:
                append_cands.append(i)
        for w in append_cands:
            q.append(((cur_e, cur_stack + (w,)), dist+1))
    ans = visited[(cur_e, tuple())]
    return ans

def solution(weights):
    E, W = len(weights), len(weights[0])

    cw = [[0] * E for _ in range(E)]
    for l in range(E):
        for r in range(l, E):
            cw[l][r] = sum([min(weight[i] for weight in weights[l:r+1]) for i in range(W)])
    cwdp = {}
    def common_weight(l, r):
        return cw[l][r]
        # if (l,r) in cwdp:
        #     return cwdp[(l,r)]
        # cwdp[(l,r)] = sum([min(weight[i] for weight in weights[l:r+1]) for i in range(W)])
        # return cwdp[(l,r)]

    dp = {}
    def subproblem(l, r):
        if (l,r) in dp:
            return dp[(l,r)]
        assert 0 <= l <= r < E
        if l == r:
            return 0
        ans = float('inf')
        for cand_mid in range(l, r):
            cand = subproblem(l, cand_mid) + subproblem(cand_mid+1, r) 
            # cost = 2 * (common_weight(l,cand_mid) + common_weight(cand_mid+1,r) - 2 * common_weight(l,r))
            cost = 2 * (cw[l][cand_mid] + cw[cand_mid+1][r] - 2 * cw[l][r])
            cand += cost
            ans = min(ans, cand)
        dp[(l,r)] = ans
        return ans

    ans = subproblem(0, E-1) + 2 * cw[0][E-1]
    return ans

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    E, W = map(int, input().split())
    weights = []
    for _ in range(E):
        weight = list(map(int,input().split()))
        weights.append(weight)
    res = solution(weights)
    print("Case #{}: {}".format(case_num, res))
