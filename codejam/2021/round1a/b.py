from __future__ import print_function
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

ans = 0
def easy_solution(hm):
    global ans
    primes = sorted(list(hm.keys()))
    counts = [hm[k] for k in primes]
    eprint(hm)
    eprint(primes)
    eprint(counts)
    # dfs
    #nums = sum([[k]*v for k,v in hm.items()], start=[])
    S, P = 0,1
    for k in primes:
        S += (k*hm[k])
    curr = [0] * len(counts)
    stack = []
    ans = 0

    def dfs(i, S, P):
        global ans
        if i == -1:
            if S == P:
                ans = max(ans, S)
            return
        for takeout in range(0, counts[i]+1):
            S2 = S - primes[i]*takeout
            P2 = P * (primes[i]**takeout)
            if S2 >= P2:
                dfs(i-1, S2, P2)

    dfs(len(curr)-1, S, P)
    return ans

def solution(hm):
    # product of numbers < 499*10^15 < 2^60 -> at most 60 cards in product group
    # sum of those numbers < 499*60 = 29940
    # answer must be between [total_sum - 29940, total_sum]
    # try each one, factorize by using only the possible primes

    PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
    def factorize(P):
        factors = collections.Counter()
        for prime in PRIMES:
            while P % prime == 0:
                factors[prime] += 1
                P //= prime
        if P != 1:
            return None
        return factors

    ans = 0
    total_sum = sum(k*v for k,v in hm.items())
    #eprint(total_sum)
    for P in range(max(2,total_sum - 29940), total_sum+1):
        factors = factorize(P)
        if factors is None:
            continue
        remaining = collections.Counter(hm)
        for factor, count in factors.items():
            if factor not in hm or hm[factor] < count:
                break
            remaining[factor] -= count
        else:
            if sum(k*v for k,v in remaining.items()) == P:
                ans = max(ans, P)
        #eprint(P, hm, factors, remaining)
    return ans

T = int(raw_input()) # read num test cases
for case_num in range(1, T + 1):
    N = int(raw_input())
    hm = {}
    for _ in range(N):
        k, v = map(int,raw_input().split())
        hm[k] = v
    res = solution(hm)
    print("Case #{}: {}".format(case_num, res))
