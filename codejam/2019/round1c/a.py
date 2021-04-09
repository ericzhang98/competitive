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

def solution(C):
    valid = set(range(len(C)))
    m = max(len(c) for c in C)
    ans = []
    for i in itertools.count():
        chars = {C[j][i % len(C[j])] for j in valid}
        if len(chars) == 3:
            return "IMPOSSIBLE"
        elif len(chars) == 1:
            if chars == {'R'}:
                selected = 'P'
                beat = 'R'
            elif chars == {'P'}:
                selected = 'S'
                beat = 'P'
            elif chars == {'S'}:
                selected = 'R'
                beat = 'S'
            else:
                raise Exception("bad2")
        elif len(chars) == 2:
            if chars == {'R', 'P'}:
                selected = 'P'
                beat = 'R'
            elif chars == {'P', 'S'}:
                selected = 'S'
                beat = 'P'
            elif chars == {'S', 'R'}:
                selected = 'R'
                beat = 'S'
            else:
                raise Exception("bad3")
        else:
            raise Exception("bad1")
        ans.append(selected)
        for j in list(valid):
            if C[j][i % len(C[j])] == beat:
                valid.remove(j)
        if len(valid) == 0:
            break
    return "".join(ans)

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    A = int(input())
    C = []
    for _ in range(A):
        C.append(input())
    res = solution(C)
    print("Case #{}: {}".format(case_num, res))
