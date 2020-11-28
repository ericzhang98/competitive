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

def solution(C, B):
    n = len(B)
    if B[0] == 0 or B[-1] == 0:
        return "IMPOSSIBLE"
    position = list(range(n))
    target = list(range(n))
    curr = 0
    height = 1
    for i, v in enumerate(B):
        while v > 0:
            target[curr] = i
            height = max(height, 1+abs(i-curr))
            curr += 1
            v -= 1
    ramps = [['.']*n for _ in range(height)]
    for i in range(height):
        for j in range(n):
            if position[j] == target[j]:
                ramps[i][position[j]] = '.'
            elif position[j] < target[j]:
                ramps[i][position[j]] = '\\'
                position[j] += 1
            elif position[j] > target[j]:
                ramps[i][position[j]] = '/'
                position[j] -= 1

    ramps_str = ["".join(row) for row in ramps]
    return "\n".join([str(height)] + ramps_str)

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    # process stdin with input()
    C = int(input())
    B = list(map(int, input().split(" ")))
    res = solution(C, B)
    print("Case #{}: {}".format(case_num, res))
