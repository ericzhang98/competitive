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

def solution(N,C):
    mi = N-1
    ma = (2+N)*(N-2+1)//2
    if C < mi or C > ma:
        return "IMPOSSIBLE"

    def solve(i,j,C):
        N = j-i+1
        if C < N-1:
            raise Exception("bad2")
        elif C == N-1:
            return list(range(i,j+1))
        elif C >= N+(N-1):
            return solve(i+1,j,C-N)[::-1] + [i]
        else:
            length = C - (N-1)
            assert(0 < length < N)
            return list(range(i+length,i-1,-1)) + list(range(i+length+1,j+1))

    return " ".join(map(str,solve(1,N,C)))

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    N, C = map(int, input().split())
    res = solution(N,C)
    print("Case #{}: {}".format(case_num, res))
