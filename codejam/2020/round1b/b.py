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

def check(x,y):
    global ANS,cnt
    cnt += 1
    if ANS is not None:
        eprint("no op")
        return True
    print(x, y, flush=True)
    res = input()
    #eprint(f"x,y: {(x,y)}")
    #eprint(f"res: {res}")
    if res == "MISS":
        return False
    elif res == "HIT":
        return True
    elif res == "CENTER":
        eprint(f"center: {x} {y}")
        ANS = (x,y)
        return True
    else:
        assert(False)

def solution():
    global ANS
    ANS = None

    guaranteed_points = [(-5*10**8,0),(5*10**8,0),(0,5*10**8),(0,-5*10**8)]
    for gp in guaranteed_points:
        if check(*gp):
            start = gp
    assert(start is not None)
    sx, sy = start

    def lasttrue(l,r,dx,dy):
        while l != r:
            m = ((l[0]+r[0]+1)//2, (l[1]+r[1]+1)//2)
            if check(*m):
                l=m
            else:
                r=(m[0]-dx,m[1]-dy)
        return l
    def firsttrue(l,r,dx,dy):
        while l != r:
            m = ((l[0]+r[0])//2, (l[1]+r[1])//2)
            if check(*m):
                r=m
            else:
                l=(m[0]+dx,m[1]+dy)
        return l

    up = lasttrue(start, (sx,1*10**9), 0, 1)
    eprint(f"up: {up}")
    eprint(f"cnt: {cnt}")
    down = firsttrue((sx,-1*10**9), start, 0, 1)
    eprint(f"down: {down}")
    eprint(f"cnt: {cnt}")
    left = firsttrue((-1*10**9,sy), start, 1, 0)
    eprint(f"left: {left}")
    eprint(f"cnt: {cnt}")
    right = lasttrue(start, (1*10**9,sy), 1, 0)
    eprint(f"right: {right}")
    eprint(f"cnt: {cnt}")

    x = (left[0] + right[0]) // 2
    y = (up[1] + down[1]) // 2

    check(x,y)
    assert(ANS is not None)

ANS = None
cnt = 0
T, A, B = map(int, input().split()) # read num test cases
for case_num in range(1, T + 1):
    solution()
