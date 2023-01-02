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

def draw_circle_filled_wrong(R):
    pixels = set()
    def draw_circle_perimeter(R):
        for x in range(-R, R+1): 
            y = round(math.sqrt(R * R - x * x))   # round to nearest integer, breaking ties towards zero
            pixels.add((x,y))
            pixels.add((x,-y))
            pixels.add((y,x))
            pixels.add((-y,x))
    for r in range(0, R+1):
        draw_circle_perimeter(r)
    return pixels

def draw_circle_filled_correct(R):
    pixels = set()
    for x in range(-R, R+1):
        for y in range(-R, R+1):
            if round(math.sqrt(x * x + y * y)) <= R:
                pixels.add((x, y))
    return pixels

def solution(R):
    ans = len(draw_circle_filled_correct(R)) - len(draw_circle_filled_wrong(R))
    return ans

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    R = int(input())
    res = solution(R)
    print("Case #{}: {}".format(case_num, res))
