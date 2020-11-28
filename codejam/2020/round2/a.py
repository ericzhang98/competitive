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

def get_n(X):
    quad = (-1 + math.sqrt(1+8*X)) / 2
    quad = math.floor(quad)
    # floating point precision check
    for cand in range(quad-1, quad+2):
        if nth(cand) <= X:
            ans = cand
    return ans
def nth(n):
    return (1+n)*n//2
def get_n2(s,X):
    quad = (-s+1 + math.sqrt((s-1)**2 + 4*X)) / 2
    quad = math.floor(quad)
    # floating point precision check
    for cand in range(quad-1, quad+2):
        if nth2(s,cand) <= X:
            ans = cand
    return ans

def nth2(s,n):
    return (s+n-1)*n

def solution(L, R):
    #print(L, R)
    """
    Ln = get_n(L)
    Rn = get_n(R)
    print(Ln,Rn)
    nthL, nthR = nth(L), nth(R)
    nthD = nthL - nthR
    print(nthL, nthR, nthD)
    """

    n = 0

    if L >= R:
        D = L - R
        n = get_n(D)
        L -= nth(n)
    else:
        D = R - L
        n = get_n(D)
        R -= nth(n)
        # R might still be one step greater, watch out for can't dec by one whole step
        if R > L:
            if R >= (n+1):
                n += 1
                R -= n
            else:
                return "{} {} {}".format(n, L, R)

    #print(L, R, n)

    # L: -n-1, -n-3, ..
    n2L = get_n2(n+1, L)
    # R: -n-2, -n-4, ..
    n2R = get_n2(n+2, R)

    n2 = min(n2L, n2R)


    L -= nth2(n+1, n2)
    R -= nth2(n+2, n2)

    #print(L, R, n2L, n2R, n2)

    n += 2*n2

    #print("n:", n)
    if L >= n+1:
        n += 1
        L -= n
        #print("bump one more L", L)

    #print("WTFFFF", n, L, R)

    return "{} {} {}".format(n, L, R)

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    L, R = list(map(int, input().split()))
    res = solution(L, R)
    print("Case #{}: {}".format(case_num, res))
