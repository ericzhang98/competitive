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

def is_roaring(num):
    s = str(num)
    for i in range(1,len(s)):
        start = int(s[:i])
        curr = str(start)
        while int(curr) <= num:
            if int(curr) == num:
                return True
            curr = curr + str(start+1)
            start += 1
    return False

def extend(start, Y):
    add = int(start) + 1
    curr = str(start)
    while int(curr) <= Y:
        curr += str(add)
        add += 1
    return int(curr)

def easy_solution(Y):
    if Y <= 10**6:
        # dumb soln
        for guess in range(Y+1, 100000000100000001):
            if is_roaring(guess):
                return guess

    if Y < 12:
        return 12

    ans = 100000000100000001
    s = str(Y)
    for i in range(1,len(s)):
        start = int(s[:i])
        ans = min(extend(start, Y), ans)
        ans = min(extend(start+1, Y), ans)
    return ans

def good_solution(Y):
    Y += 1
    ans = 1234567891011121314

    def bsearch(prefix_length, concat_times):
        def gen(start):
            return int("".join([str(x) for x in range(start, start+concat_times)]))
        lo, hi = int('1' + '0'*(prefix_length-1)), int('9'*prefix_length)
        while lo < hi:
            mi = (lo + hi) // 2
            if gen(mi) >= Y:
                hi = mi
            else:
                lo = mi+1
        return gen(lo)

    for prefix_length in range(1,10):
        for concat_times in range(2, 15):
            cand = bsearch(prefix_length, concat_times)
            if cand >= Y:
                #eprint(prefix_length, concat_times, cand)
                ans = min(ans, cand)
    return ans

def solution(Y):
    Y += 1
    ans = float('inf')

    def bsearch(concat_times):
        def gen(start):
            return int("".join([str(x) for x in range(start, start+concat_times)]))
        lo, hi = 1, 10**9
        while lo < hi:
            mi = (lo + hi) // 2
            if gen(mi) >= Y:
                hi = mi
            else:
                lo = mi+1
        return gen(lo)

    for concat_times in range(2, 15):
        cand = bsearch(concat_times)
        if cand >= Y:
            ans = min(ans, cand)
    return ans


LIMIT = 10**18
ONES = 14
roaring_years = []

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    Y = int(input())
    res = solution(Y)
    print("Case #{}: {}".format(case_num, res))
