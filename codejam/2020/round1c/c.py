import sys
import collections
import heapq
import itertools
import bisect
import fractions
import math
import functools

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def basic_solution(D, A):
    if D == 2:
        if len(set(A)) == len(A): return 1
        else: return 0
    if D == 3:
        cnts = collections.Counter(A)
        sizes = sorted(cnts.keys())
        most_common = cnts.most_common()
        best = 0
        if most_common[0][1] >= 3: return 0
        for s in sizes:
            if s % 2 == 0 and s // 2 in cnts:
                return 1
            if best == 2:
                return 1
            best = max(best, cnts[s])
        return 2
    A = sorted(A)
    return 0

def solution(D, A):
    A.sort()

    lcm = functools.reduce(lambda x, y: abs(x * y) // math.gcd(x, y), range(2, D + 1))
    A = [a*lcm for a in A]
    l, r = 1, A[-1]
    def check(m):
        return sum(a // m for a in A) >= D
    while l < r:
        m = (l+r+1)//2
        if check(m):
            l = m
        else:
            r = m-1
    ma = l

    full = collections.Counter()
    slices = collections.Counter()
    for a in A:
        for d in range(1,D+1):
            g = math.gcd(a,d)
            slice_size = (a // g, d // g)
            if a // d > ma: continue
            if slices[slice_size] + d <= D:
                full[slice_size] += 1
                slices[slice_size] += d

    ans = D - max(full.values())
    return ans

T = int(input()) # read num test cases
for case_num in range(1, T + 1):

    arr = input().split(" ")
    N, D = int(arr[0]), int(arr[1])
    A = list(map(int, input().split(" ")))

    res = solution(D, A)
    print("Case #{}: {}".format(case_num, res))
