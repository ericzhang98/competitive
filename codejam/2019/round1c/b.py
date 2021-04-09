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

def query(i):
    assert(1 <= i <= 595)
    print(f"{i}")
    res = input()
    if res == 'N':
        raise Exception("bad query")
    return res

def solve():
    ans = []
    remaining = {'A', 'B', 'C', 'D', 'E'}
    cands = list(range(119))
    for pos in range(4):
        hm = {k: [] for k in remaining}
        for i in cands:
            res = query(1 + i*5 + pos)
            hm[res].append(i)
        _, k = min((len(v), k) for k, v in hm.items())
        ans.append(k)
        remaining.remove(k)
        cands = hm[k]
    ans.append(list(remaining)[0])
    return "".join(ans)

T, _ = map(int, input().split()) # read num test cases
for case_num in range(1, T + 1):
    ans = solve()
    print(ans)
    res = input()
    if res == 'N':
        raise Exception("wrong ans")
