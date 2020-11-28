#!/usr/local/bin/python3
import sys
import collections
import heapq
import itertools
import bisect

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

SAME = 0
DIFF = 1

def solution(*args):

    if B == 10:
        bits = []
        for i in range(1, 11):
            print(i, flush=True)
            response = int(input())
            bits.append(response)
        ans = "".join(map(str, bits))
        print(ans, flush=True)
        return

    """
    num_groups = B // 5
    group_diff = [[0]*4 for _ in range(num_groups)]
    opp_diff = [0] * (B // 2)
    flip_group = dict()

    for group in range(num_groups):
        groupl = group
        groupr = num_groups - group
        prevl = None
        prevr = None
        xorbit = None
        revbit = None
        for i in range(5):
            bl = group*5 + i
            br = B - bl
            print(bl+1, flush=True)
            l = int(input())
            print(br+1, flush=True)
            r = int(input())

            if l == r:
                opp_diff[bl] = SAME
                xorbit = bl
            else:
                opp_diff[bl] = DIFF
                revbit = bl
            if i >= 1:
                group_diff[groupl][i-1] = SAME if l == prevl else DIFF
                group_diff[groupr][4-i] = SAME if r == prevr else DIFF
            prevl = l
            prevr = r

        if xorbit != None and revbit != None
            flip_group[group] = (xorbit, revbit)
    """

    xorbit = None
    revbit = None
    opp_diff = [0] * (B // 2)
    for i in range(B // 2):
        bl = i
        br = B - i
        print(bl+1, flush=True)
        l = int(input())
        print(br+1, flush=True)
        r = int(input())
        if l == r:
            opp_diff[bl] = SAME
            xorbit = bl
        else:
            opp_diff[bl] = DIFF
            revbit = bl


    print("0"*B, flush=True)
    return

T, B = map(int, input().split(" "))
for case_num in range(1, T + 1):

    solution()

    response = input()
    if response != "Y" : sys.exit()
