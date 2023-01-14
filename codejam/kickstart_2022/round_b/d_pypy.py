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

def solution(A, R, C):
    dij = [(-1,0), (1,0), (0,-1), (0,1)]

    all_valid = set()
    for i in range(R):
        for j in range(C):
            if A[i][j] == '*':
                all_valid.add((i,j))
    def check_valid():
        visited = set()
        def dfs(i,j):
            if (i,j) in visited:
                return
            visited.add((i,j))
            for di, dj in dij:
                i2, j2 = i+di, j+dj
                if 0<=i2<R and 0<=j2<C and A[i2][j2] == '*' and (i2,j2):
                    dfs(i2,j2)
        dfs(0,0)
        return visited == all_valid
    if not check_valid():
        return "IMPOSSIBLE"

    # cycle expansion dfs via pointers
    pointers = [[''] * (2*C) for _ in range(2*R)]
    for i in range(R):
        for j in range(C):
            pointers[2*i][2*j] = 'S'
            pointers[2*i+1][2*j] = 'E'
            pointers[2*i+1][2*j+1] = 'N'
            pointers[2*i][2*j+1] = 'W'
    visited = {(0,0)}
    def dfs(i, j):
        assert (i,j) in visited
        for di, dj in dij:
            i2, j2 = i+di, j+dj
            if 0<=i2<R and 0<=j2<C and A[i2][j2] == '*' and (i2,j2) not in visited:
                visited.add((i2,j2))
                if (di,dj) == (1,0):
                    pointers[2*i+1][2*j] = 'S'
                    pointers[2*i2][2*j2+1] = 'N'
                elif (di,dj) == (-1,0):
                    pointers[2*i2+1][2*j2] = 'S'
                    pointers[2*i][2*j+1] = 'N'
                elif (di,dj) == (0,1):
                    pointers[2*i+1][2*j+1] = 'E'
                    pointers[2*i2][2*j2] = 'W'
                elif (di,dj) == (0,-1):
                    pointers[2*i2+1][2*j2+1] = 'E'
                    pointers[2*i][2*j] = 'W'
                else: assert False
                dfs(i2,j2)
    dfs(0,0)
    assert visited == all_valid

    ans = []
    curx, cury = 0,0
    while True:
        direction = pointers[curx][cury]
        ans.append(direction)
        if direction == 'S':
            curx += 1
        elif direction == 'N':
            curx -= 1
        elif direction == 'E':
            cury += 1
        elif direction == 'W':
            cury -= 1
        else: assert False
        if (curx, cury) == (0,0):
            break
    assert len(ans) == 4 * len(visited)

    return "".join(ans)

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    R, C = map(int, input().split())
    A = []
    for _ in range(R):
        A.append(list(input()))
    res = solution(A, R, C)
    print("Case #{}: {}".format(case_num, res))
