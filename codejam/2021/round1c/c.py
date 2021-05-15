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

def flip(b):
    return "".join({'0': '1', '1': '0'}[c] for c in b)

def fix(b):
    while b and b[0] == '0':
        b = b[1:]
    if b == "":
        return "0"
    return b

def easy_solution(S, E):
    if S == E:
        return 0

    h = [S]
    seen = set()
    for dist in range(25):
        nxt = []
        #eprint(h)
        for curr in h:
            if curr in seen: continue
            seen.add(curr)
            if curr == E:
                return dist
            a = fix(curr + "0")
            if a not in seen:
                nxt.append(a)
            b = fix(flip(curr))
            if b not in seen:
                nxt.append(b)
        h = nxt

    return "IMPOSSIBLE"

def solution(S, E):
    """
    double: append 1 if len(arr) odd else inc arr[-1] by 1 if len(arr) even
    flip: arr.pop(0)
    
    if starting bit groups has ceil(len, next even num) < ending bit groups, IMPOSSIBLE

    """

    offset = 0

    # handle E == 0
    if E == "0":
        if S == "0":
            return 0
        groups = [len(list(g)) for k, g in itertools.groupby(S)]
        return len(groups)

    # handle S == 0
    if S == "0":
        if E == "0":
            return 0
        # first operation must be a flip to turn into 1
        offset += 1
        S = "1"

    S = [len(list(g)) for k, g in itertools.groupby(S)]
    E = [len(list(g)) for k, g in itertools.groupby(E)]

    """
    if len(S) even, then len(E) <= len(S)
    if len(S) odd, then len(E) <= len(S) + 1
        - if len(E) == len(S) + 1, first op must be double to append 1
    """
    if (len(S) + (len(S) % 2)) < len(E):
        return "IMPOSSIBLE"
    if len(S) + 1 == len(E):
        offset += 1
        S.append(1)

    """
    when am I allowed to fix the cand's last group
    - if len(S) is even, always fixable
    - if len(S) is odd
        - if len(S) > len(E), then flip to S.pop(0), len(S) is now even, fix
        - if len(S) == len(E), then can't do anything
    alignment possiblities
    if len S is even, S[-1] can be <= corresponding E group, since we can fix
    if len S is odd, S[-1] can be <= correspoding E group, if len(S) > len(E), since we can pop(0) and then fix
    """

    """
    # brute force each possible alignment for S[i:] == E
    # S[i:] == E[:len(S[i:])] or S[i:-1] == E[:len(S[i:])-1] if fixable
    # len(S[i:]) <= len(E)
    """

    ans = (len(S) - len(E)) + sum(E) + len(E)

    for i in range(len(S)-len(E), len(S)):
        cand = S[i:]
        if cand == E[:len(cand)]:
            ans2 = (len(S) - len(E)) + sum(E[len(cand):]) + len(E[len(cand):])
            ans = min(ans, ans2)
        if len(S) % 2 == 0 or len(S) > len(E):
            if len(cand) > 1:
                if cand[:-1] == E[:len(cand)-1]:
                    if cand[-1] <= E[len(cand)-1]:
                        ans2 = (len(S) - len(E)) + sum(E[len(cand):]) + len(E[len(cand):]) + (E[len(cand)-1] - cand[-1])
                        ans = min(ans, ans2)
            else:
                if cand[-1] <= E[len(cand)-1]:
                    ans2 = (len(S) - len(E)) + sum(E[len(cand):]) + len(E[len(cand):]) + (E[len(cand)-1] - cand[-1])
                    ans = min(ans, ans2)
        """
        if len(cand) > 1:
            if cand[:-1] == E[:len(cand)-1]:
                if len(S) % 2 == 0 or len(S) > len(E):
                    pass
        else:
            if len(S) % 2 == 0 or len(S) > len(E):
                pass
        """

    return ans + offset


T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    S, E = input().split()
    res = solution(S, E)
    print("Case #{}: {}".format(case_num, res))
