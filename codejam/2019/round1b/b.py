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

def query(x):
    print(x, flush=True)
    res = int(input())
    return res

def solution():
    ans = [0]*6
    res = query("220")
    ans[3] = res // 2**55
    ans[4] = (res % (2**55)) // 2**44
    ans[5] = (res % (2**44)) // 2**36
    res = query("56")
    res -= (ans[3]*2**14 + ans[4]*2**11 + ans[5]*2**9)
    ans[0] = res // 2**56
    ans[1] = (res % (2**56)) // 2**28
    ans[2] = (res % (2**28)) // 2**18
    res = query(" ".join([str(x) for x in ans]))
    if res == -1:
        sys.exit()

T, W = map(int, input().split())
for case_num in range(1, T + 1):
    res = solution()
