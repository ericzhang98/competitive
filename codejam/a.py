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

def getmin(start, end):
    print(f"M {start+1} {end+1}")
    res = int(input())
    if res == -1:
        raise Exception("bad1")
    return res - 1

def swap(start, end):
    print(f"S {start+1} {end+1}")
    res = int(input())
    if res == -1:
        raise Exception("bad2")

def finish():
    print("D")
    res = int(input())
    if res == -1:
        raise Exception("bad3")

def solution():
    for idx in range(99):
        mi_idx = getmin(idx, 99)
        if mi_idx != idx:
            swap(idx, mi_idx)
    finish()

T, N = map(int, input().split())
for case_num in range(1, T + 1):
    solution()
