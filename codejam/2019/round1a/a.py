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

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution(R,C):
    def valid(a,b):
        return not any([a[0] == b[0], a[1] == b[1], a[0] - a[1] == b[0] - b[1], a[0] + a[1] == b[0] + b[1]])
    for seed in range(100):
        random.seed(seed)
        ans = []
        cells = [(i,j) for i in range(1,R+1) for j in range(1,C+1)]
        while len(cells) > 0:
            random.shuffle(cells)
            if len(ans) == 0:
                choice = cells.pop(0)
            else:
                for i in range(len(cells)):
                    if valid(cells[i], ans[-1]):
                        choice = cells.pop(i)
                        break
                else:
                    break
            ans.append(choice)
        if len(cells) == 0:
            return "POSSIBLE\n" + "\n".join([f"{i} {j}" for i,j in ans])
    return "IMPOSSIBLE"

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    R, C = map(int, input().split())
    res = solution(R,C)
    print("Case #{}: {}".format(case_num, res))
