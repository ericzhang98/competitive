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
# codejam pypy only has 5311 recursion limit and does not change

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution("params"):
    print("params")
    # TODO
    return 0

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    # process stdin with input()
    # TODO
    res = solution("params")
    print("Case #{}: {}".format(case_num, res))
