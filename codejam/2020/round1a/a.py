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

def solution(P):
    prefixes, suffixes, mids = [], [], []
    for pattern in P:
        pattern = pattern.split('*')
        prefix = pattern[0]
        suffix = pattern[-1]
        mid = "".join(pattern[1:len(pattern)-1])
        prefixes.append(prefix)
        suffixes.append(suffix)
        mids.append(mid)
    prefixes.sort(key=len)
    suffixes.sort(key=len)
    a = prefixes[-1]
    for prefix in prefixes:
        if prefix != a[:len(prefix)]:
            return "*"
    b = suffixes[-1]
    for suffix in suffixes:
        if suffix != b[len(b)-len(suffix):]:
            return "*"
    return a + "".join(mids) + b

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    N = int(input())
    P = []
    for _ in range(N): P.append(input())
    res = solution(P)
    print("Case #{}: {}".format(case_num, res))
