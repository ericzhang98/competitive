import sys
import collections
import heapq
import itertools
import bisect

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution(X,Y,S):
    # for each ith endpoint can I reach that point in i steps
    dx, dy = X, Y
    if dx == 0 and dy == 0: return 0
    for i, c in enumerate(list(S)):
        if c == 'N':
            dy += 1
        elif c == 'S':
            dy -= 1
        elif c == 'E':
            dx += 1
        elif c == 'W':
            dx -= 1
        if abs(dx) + abs(dy) <= i+1:
            return i+1
    return "IMPOSSIBLE"

T = int(input()) # read num test cases
for case_num in range(1, T + 1):

    arr = input().split(" ")
    X, Y, S = int(arr[0]), int(arr[1]), arr[2]
    res = solution(X, Y, S)
    print("Case #{}: {}".format(case_num, res))
