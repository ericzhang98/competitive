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

def slow_solution(mat):
    R, C = len(mat), len(mat[0])
    N = R*C
    interest = 0

    def compass(i,j):
        l = []
        for i2 in range(i-1,-1,-1):
            if mat[i2][j] != 0:
                l.append(mat[i2][j])
                break
        for i2 in range(i+1,R):
            if mat[i2][j] != 0:
                l.append(mat[i2][j])
                break
        for j2 in range(j-1,-1,-1):
            if mat[i][j2] != 0:
                l.append(mat[i][j2])
                break
        for j2 in range(j+1,C):
            if mat[i][j2] != 0:
                l.append(mat[i][j2])
                break
        return l

    go = True
    while go:
        go = False
        interest += sum(sum(row) for row in mat)
        mat2 = copy.deepcopy(mat)
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0: continue
                l = compass(i,j)
                avg = sum(l) / len(l) if len(l) > 0 else float('-inf')
                if mat[i][j] < avg:
                    mat2[i][j] = 0
                    go = True
        mat = mat2

    return interest

def solution(mat):
    R, C = len(mat), len(mat[0])

    def bounds(l):
        return [(i,j) if 0 <= i < R and 0 <= j < C else None for i,j in l]

    def avg(l):
        l = [x for x in l if x is not None]
        l = [mat[i][j] for i,j in l]
        return sum(l) / len(l) if len(l) > 0 else float('-inf')

    def rm(pos):
        N,S,W,E = neigh[pos]
        if N is not None:
            neigh[N][1] = S
        if S is not None:
            neigh[S][0] = N
        if W is not None:
            neigh[W][3] = E
        if E is not None:
            neigh[E][2] = W

    neigh = {} # N, S, W, E
    rounds = {}
    curr = set()
    for i in range(R):
        for j in range(C):
            pos = (i,j)
            neigh[pos] = bounds([(i-1,j), (i+1,j), (i,j-1), (i,j+1)])
            if mat[i][j] < avg(neigh[pos]):
                curr.add(pos)
    r = 1
    while curr:
        cands = set()
        for pos in curr:
            rounds[pos] = r
            nei = neigh[pos]
            rm(pos)
            for cand in nei:
                if cand is not None:
                    cands.add(cand)
        nxt = set()
        for cand in cands:
            if cand not in rounds:
                i, j = cand
                if mat[i][j] < avg(neigh[cand]):
                    nxt.add(cand)
        curr = nxt
        r += 1

    ans = 0
    ma = max(rounds.values(), default=0) + 1
    for i in range(R):
        for j in range(C):
            ans += (rounds[(i,j)] if (i,j) in rounds else ma) * mat[i][j]

    return ans


T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    R, C = map(int, input().split())
    mat = []
    for _ in range(R):
        mat.append(list(map(int, input().split())))
    res = solution(mat)
    print("Case #{}: {}".format(case_num, res))
