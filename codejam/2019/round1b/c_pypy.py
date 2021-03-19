from __future__ import print_function
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

def solution(N,O,C,D):
    K = int(math.ceil(math.log(N+1,2)))
    RMQC = [[0 for _ in range(K)] for _ in range(N)]
    RMQD = [[0 for _ in range(K)] for _ in range(N)]
    for i in range(N):
        RMQC[i][0] = C[i]
        RMQD[i][0] = D[i]
    for k in range(1, K):
        for i in range(0, N-2**k+1):
            RMQC[i][k] = max(RMQC[i][k-1], RMQC[i+2**(k-1)][k-1])
            RMQD[i][k] = max(RMQD[i][k-1], RMQD[i+2**(k-1)][k-1])
    
    def rmquery(RMQ, i, j):
        length = j-i
        if length == 0: return float('-inf')
        k = int(math.floor(math.log(length,2)))
        left = RMQ[i][k]
        right = RMQ[j-2**k][k]
        return max(left, right)

    def subsolve(i):
        # optimization
        if C[i] + O < D[i]:
            return 0

        # Li, Ri limits where max([C[Li]..C[Ri-1]]) == C[i]
        lo, hi = 0, i
        while lo < hi:
            mi = (lo + hi) // 2
            if mi == i or rmquery(RMQC, mi, i) < C[i]:
                hi = mi
            else:
                lo = mi+1
        Li = lo
        lo, hi = i, N-1
        while lo < hi:
            mi = (lo + hi + 1) // 2
            if rmquery(RMQC, i, mi+1) <= C[i]:
                lo = mi
            else:
                hi = mi-1
        Ri = lo+1

        # Ai, Bi limits where max([D[Ai]..D[Bi-1]]) <= C[i] + O
        lo, hi = Li, i+1
        while lo < hi:
            mi = (lo + hi) // 2
            if rmquery(RMQD, mi, i+1) <= C[i] + O:
                hi = mi
            else:
                lo = mi+1
        Ai = lo
        lo, hi = i, Ri
        while lo < hi:
            mi = (lo + hi + 1) // 2
            if rmquery(RMQD, i, mi) <= C[i] + O:
                lo = mi
            else:
                hi = mi-1
        Bi = lo

        # Xi, Yi limits where max([D[Xi]..D[Yi-1]]) <= C[i] - O
        lo, hi = Li, i+1
        while lo < hi:
            mi = (lo + hi) // 2
            if rmquery(RMQD, mi, i+1) < C[i] - O:
                hi = mi
            else:
                lo = mi+1
        Xi = lo
        lo, hi = i, Ri
        while lo < hi:
            mi = (lo + hi + 1) // 2
            if rmquery(RMQD, i, mi) < C[i] - O:
                lo = mi
            else:
                hi = mi-1
        Yi = lo

        a = (i+1 - Ai) * (Bi - i)
        b = (i+1 - Xi) * (Yi - i)
        ans = a - b

        #eprint(f"--i={i},Li={Li},Ri={Ri},Ai={Ai},Bi={Bi},Xi={Xi},Yi={Yi},a={a},b={b},ans={ans}")

        return ans

    ans = 0
    for i in range(N):
        ans += subsolve(i)
    return ans

T = int(raw_input()) # read num test cases
for case_num in range(1, T + 1):
    N, O = map(int, raw_input().split())
    C = list(map(int, raw_input().split()))
    D = list(map(int, raw_input().split()))
    res = solution(N, O, C, D)
    print("Case #{}: {}".format(case_num, res))
