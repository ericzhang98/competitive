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

def solution(L):
    N = len(L)
    ans = 0
    for i in range(N-1):
        j = L.index(min(L[i:]))
        ans += (j-i+1)
        L = L[:i] + L[i:j+1][::-1] + L[j+1:]
    return ans

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    N = int(input())
    L = list(map(int,input().split()))
    res = solution(L)
    print("Case #{}: {}".format(case_num, res))
