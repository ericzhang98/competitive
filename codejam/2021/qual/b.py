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

def solution_easy(X,Y,S):
    ans = 0
    curr = None
    for c in S:
        if c == 'J' and curr == 'C':
            ans += X
        elif c == 'C' and curr == 'J':
            ans += Y
        if c != '?':
            curr = c
    return ans

def solution(X,Y,S):
    if X >= 0 and Y >= 0:
        return solution_easy(X,Y,S)
    else:
        sys.setrecursionlimit(1000000)
        @functools.lru_cache(None)
        def optimal_segment(n,left,right):
            if left == None or right == None:
                print(n,left,right)
                raise Exception("asdf")
            if n == 0:
                if left == right:
                    return 0
                elif left == 'C' and right == 'J':
                    return X
                elif left == 'J' and right == 'C':
                    return Y
            else:
                if right == 'C':
                    return min(optimal_segment(n-1,left,'C'), optimal_segment(n-1,left,'J')+Y)
                elif right == 'J':
                    return min(optimal_segment(n-1,left,'J'), optimal_segment(n-1,left,'C')+X)
        def optimal_segment_all(n,left,right):
            if left == None and right == None:
                if n >= 2:
                    return min(optimal_segment(n-2,a,b) for a,b in itertools.product(['C', 'J'], repeat=2))
                else:
                    return 0
            elif left == None:
                if n >= 1:
                    return min(optimal_segment(n-1,'C',right), optimal_segment(n-1,'J',right))
                else:
                    return 0
            elif right == None:
                if n >= 1:
                    return min(optimal_segment(n-1,left,'C'), optimal_segment(n-1,left,'J'))
                else:
                    return 0
            else:
                return optimal_segment(n,left,right)
        ans = 0
        prv = None
        qcnt = 0
        for curr in [None] + list(S) + [None]:
            if curr != '?':
                ans += optimal_segment_all(qcnt,prv,curr)
                prv = curr
                qcnt = 0
            else:
                qcnt += 1
        return ans

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    X,Y,S = input().split()
    res = solution(int(X), int(Y), S)
    print("Case #{}: {}".format(case_num, res))
