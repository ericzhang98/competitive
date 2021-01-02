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

def query(m):
    print(" ".join([f"{m}"]*18), flush=True)
    res = list(map(int, input().split()))
    res = sum(res) % m
    return res

def sieve(n,m,nums):
    return {x for x in nums if x % m == n}

def solution():
    nums = set(range(1,1000001))
    res = query(18)
    nums = sieve(res, 18, nums)
    for _ in range(6):
        bestm = None
        mincnt = float('inf')
        for m in range(2,19):
            cnts = collections.Counter()
            for x in nums:
                cnts[x % m] += 1
            cand = max(cnts.values())
            if cand < mincnt:
                mincnt, bestm = cand, m
        res = query(bestm)
        nums = sieve(res, bestm, nums)
        eprint(res, bestm, len(nums))

    eprint(len(nums))
    eprint(f"ans: {list(nums)[0]}")
    if len(nums) == 1:
        print(list(nums)[0], flush=True)
        res = int(input())
        if res != 1:
            sys.exit()
    else:
        sys.exit()

T,N,M = map(int, input().split())
for case_num in range(1, T + 1):
    solution()

