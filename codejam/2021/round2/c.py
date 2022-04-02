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

MOD = 1000000007

# nCk with MOD
fact = [1, 1]
inv = [0, 1]
inv_fact = [1, 1]
def nCk(n, k):
    while len(inv) <= n:  # lazy initialization
        fact.append(fact[-1]*len(inv) % MOD)
        inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
        inv_fact.append(inv_fact[-1]*inv[-1] % MOD)
    return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD

def solution(l):
    l = [(x, -i, i) for i, x in enumerate(l)]

    # build RMQ
    N = len(l)
    K = int(math.ceil(math.log(N+1,2)))
    RMQ = [[0 for _ in range(K)] for _ in range(N)]
    for i in range(N):
        RMQ[i][0] = l[i]
    for k in range(1, K):
        for i in range(0, N-2**k+1):
            RMQ[i][k] = min(RMQ[i][k-1], RMQ[i+2**(k-1)][k-1])
    def rmquery(i, j):
        length = j-i
        if length == 0: return None
        k = int(math.floor(math.log(length,2)))
        left = RMQ[i][k]
        right = RMQ[j-2**k][k]
        return min(left, right)

    """
    # MLE because of recursive calls
    sys.setrecursionlimit(200000)
    def solve(i, j, target, rec):
        # eprint(i,j, rec)
        if i > j:
            return 1
        if i == j:
            return 1 if l[i][0] == target else 0
        # min is largest pancake in this segment
        v, _, min_index = rmquery(i, j+1)
        if v != target:
            return 0
        num_left = solve(i, min_index-1, target, rec+1) if i <= min_index-1 else 1
        num_right = solve(min_index+1, j, target+1, rec+1) if min_index+1 <= j else 1
        #eprint(i, j, min_index, num_left, num_right)
        return nCk(j-i+1-1, min_index-1-i+1) * num_left * num_right

    ans = solve(0, len(l)-1, 1, 0)
    return ans % MOD
    """

    stack = [(0, len(l)-1, 1, 0)]
    ans = 1
    while stack:
        i,j,target,rec = stack.pop()
        if i > j:
            continue
        if i == j:
            if l[i][0] != target:
                return 0
            continue
        # min is largest pancake in this segment
        v, _, min_index = rmquery(i, j+1)
        if v != target:
            return 0
        stack.append((i, min_index-1, target, rec+1))
        stack.append((min_index+1, j, target+1, rec+1))
        ans = (ans * nCk(j-i+1-1, min_index-1-i+1)) % MOD

    return ans % MOD

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    N = input()
    l = list(map(int,input().split()))
    res = solution(l)
    print("Case #{}: {}".format(case_num, res))
