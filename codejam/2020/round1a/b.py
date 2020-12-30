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

def nCk(n, k):
    if k == 0: return 1
    return n * nCk(n-1, k-1) / k

def solution(N):
    if N <= 500:
        ans = []
        for i in range(1,N+1):
            ans.append((i,1))
    else:
        ans = []
        N2 = N - 30
        b = format(N2, 'b')
        b = list(b)[::-1]
        rows = {i+1 for i, x in enumerate(b) if x == '1'}
        extras = sum(x == '0' for x in  b)
        assert(len(rows) + extras == len(b))
        curr = (1,1)
        ans.append(curr)
        rows.discard(1)
        while len(rows) > 0:
            r, c = curr
            r += 1
            if c != 1:
                c += 1
                assert(r == c)
            if r in rows:
                if c == 1:
                    for i in range(1, r+1):
                        ans.append((r,i))
                    curr = (r,r)
                else:
                    for i in range(r, 0, -1):
                        ans.append((r,i))
                    curr = (r,1)
                rows.remove(r)
            else:
                ans.append((r,c))
                curr = (r,c)
        for _ in range(30 - extras):
            r, c = curr
            r += 1
            if c != 1:
                c += 1
                assert(r == c)
            ans.append((r,c))
            curr = (r,c)

    amt = int(sum(nCk(n-1,k-1) for n,k in ans))
    assert(amt == N)

    ans = "\n" + "\n".join([f"{a} {b}" for a, b in ans])
    return ans

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    N = int(input())
    res = solution(N)
    print("Case #{}: {}".format(case_num, res))
