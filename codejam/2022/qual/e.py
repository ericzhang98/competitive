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

def read():
    inp = input().split()
    if len(inp) == 1:
        assert False
    cave, passage = map(int,inp)
    return cave, passage

def teleport(x):
    print(f"T {x}")

def walk():
    print("W")

def answer(x):
    print(f"E {x}")

def solution():
    N, K = map(int, input().split())
    teleport_cnts = {}
    walk_cnts = {}
    cave, passage = read()
    teleport_cnts[cave] = passage
    order = list(range(1,N+1))
    random.shuffle(order)

    for _ in range(K // 2):
        x = 1
        while order:
            cand = order.pop()
            if cand not in teleport_cnts and cand not in walk_cnts:
                x = cand
                break
        teleport(x)
        cave, passage = read()
        teleport_cnts[cave] = passage
        walk()
        cave, passage = read()
        walk_cnts[cave] = passage
    teleport_total = 0
    for cave in range(1,N+1):
        if cave in teleport_cnts:
            teleport_total += teleport_cnts[cave]
    teleport_avg_deg = teleport_total // len(teleport_cnts)
    guess = 0
    for cave in range(1,N+1):
        if cave in walk_cnts:
            guess += walk_cnts[cave]
        elif cave in teleport_cnts:
            guess += teleport_cnts[cave]
        else:
            guess += teleport_avg_deg
    guess //= 2
    answer(guess)

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    solution()
