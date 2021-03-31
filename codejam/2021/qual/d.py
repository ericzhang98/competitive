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

def query(a,b,c):
    print(f"{a} {b} {c}")
    res = int(input())
    if res == -1:
        raise Exception("bad query")
    return res

def solution(N):
    l = list(range(1,N+1))
    def solve(l):
        if len(l) <= 2:
            #eprint(f"l: {l}, ans: {l}")
            return l
        else:
            a,b,c = l[:3]
            median = query(a,b,c)
            bounds = [a,b,c]
            bounds.remove(median)
            a,c = bounds
            b = median
            left, mid, right = [], [b], []
            for x in l[3:]:
                median = query(a,c,x)
                if median == x:
                    mid.append(x)
                elif median == a:
                    left.append(x)
                elif median == c:
                    right.append(x)
            left = solve(left)
            mid = solve(mid)
            right = solve(right)
            if len(left) > 1:
                x,y = left[0], left[-1]
                median = query(x,y,a)
                if median == x:
                    left = left[::-1]
            if len(mid) > 1:
                x,y = mid[0], mid[-1]
                median = query(x,y,c)
                if median == x:
                    mid = mid[::-1]
            if len(right) > 1:
                x,y = right[0], right[-1]
                median = query(c,x,y)
                if median == y:
                    right = right[::-1]
            #eprint(f"l: {l}, ans: {left + [a] + mid + [c] + right}")
            return left + [a] + mid + [c] + right
    return solve(l)


T,N,Q = map(int,input().split())
for case_num in range(1, T + 1):
    ans = solution(N)
    print(" ".join(map(str,ans)))
    res = int(input())
    if res == -1:
        raise Exception("wrong answer")
