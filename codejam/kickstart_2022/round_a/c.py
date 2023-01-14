import sys
import copy
import operator
import math
import collections
import heapq
import itertools
import functools
import bisect
import random

sys.setrecursionlimit(1000000000)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution(S):
    N = len(S)
    if N < 5:
        return "POSSIBLE"

    def is_palindrome(cand):
        return cand == cand[::-1]

    # dp = dict()
    # for k in [format(x, 'b').zfill(4) for x in range(0, 16)]:
    #     dp[k] = False
    possible_starting = [S[:5]]
    while True:
        breakout = True
        for s in list(possible_starting):
            if '?' in s:
                breakout = False
                possible_starting.remove(s)
                idx = s.index('?')
                possible_starting.append(s[:idx] + '0' + s[idx+1:])
                possible_starting.append(s[:idx] + '1' + s[idx+1:])
        if breakout: break
    possible_starting = [s for s in possible_starting if not is_palindrome(s)]
    cur = possible_starting
    for i in range(5, N):
        # eprint(cur)
        nxt = []
        possible_chars = ['0', '1'] if S[i] == '?' else [S[i]]
        for possible_char in possible_chars:
            for k in cur:
                cand = k + possible_char
                assert(len(cand) == 6)
                # eprint(i, cand, not is_palindrome(cand))
                if not is_palindrome(cand) and not is_palindrome(cand[1:]):
                    nxt.append(cand[1:])
        cur = nxt
    # eprint(cur)
    return "POSSIBLE" if len(cur) > 0 else "IMPOSSIBLE"

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    N = int(input())
    S = input()
    res = solution(S)
    print("Case #{}: {}".format(case_num, res))
