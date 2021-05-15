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

def solution(a,b,reqs):
    reqs = tuple(list(reqs))
    n = len(reqs)
    #eprint(reqs)
    for base in range(n,n+1000):
        def works(base):
            #eprint(f"trying {base}")
            current = [0]*(base+1)
            current[base] = 1
            for i in range(base,0,-1):
                if current[i] > 0:
                    if i >= n:
                        c = current[i]
                        current[i] -= c
                        if i-b >= 0:
                            current[i-b] += c
                        if i-a >= 0:
                            current[i-a] += c
                    elif current[i] > reqs[i]:
                        c = current[i] - reqs[i]
                        current[i] -= c
                        if i-b >= 0:
                            current[i-b] += c
                        if i-a >= 0:
                            current[i-a] += c
            if all(reqs[i] <= current[i] for i in range(n)):
                return True
            else:
                return False
        if works(base):
            return base+1
    return "IMPOSSIBLE"

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    n, a, b = map(int, input().split())
    reqs = map(int, input().split())
    res = solution(a,b,reqs)
    print("Case #{}: {}".format(case_num, res))
