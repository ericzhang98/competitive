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

def solution(a,b,c):
    NUM_TICKS = 360*12*10**10
    def get_actual_pred(h,m,s):
        time_in_nano = h
        time_in_sec = time_in_nano // 10**9
        time_in_min = time_in_nano // (60*10**9)
        pred_hour = time_in_min // 60
        pred_minutes = time_in_min % 60
        pred_seconds = time_in_sec % 60
        pred_nano = time_in_nano % (10**9)
        actual_hour = h // (NUM_TICKS // 12)
        actual_minutes = m // (NUM_TICKS // 60)
        actual_seconds = s // (NUM_TICKS // 60)
        actual_nano = (s // 720) - actual_seconds*10**9
        actual = (actual_hour, actual_minutes, actual_seconds, actual_nano)
        pred = (pred_hour, pred_minutes, pred_seconds, pred_nano)
        return actual, pred

    for h,m,s in itertools.permutations([a,b,c]):
        def solve(h,m,s):
            """
            def attempt(angle,h,m,s):
                h,m,s = map(lambda x: (x + angle) % NUM_TICKS, [h,m,s])
                actual, pred = get_actual_pred(h,m,s)
                eprint(angle, actual, pred, actual <= pred)
                if actual >= pred:
                    return True
                else:
                    return False
            lo, hi = 0, NUM_TICKS - 1
            while lo < hi:
                mi = (lo+hi) // 2
                if attempt(mi,h,m,s):
                    hi = mi
                else:
                    lo = mi+1
            return lo
            return 0
            """
            angle_cands = []
            for hour_cand in range(0,12):
                diff = (-(h-m-hour_cand*3600*10**9)) % NUM_TICKS
                if diff % 11 == 0:
                    nanos_after_hour = diff // 11
                    angle = (h - (hour_cand*3600*10**9 + nanos_after_hour)) % NUM_TICKS
                    angle_cands.append(angle)
            return angle_cands

        angle_cands = solve(h,m,s)
        for angle in angle_cands:
            eprint(f"try angle {angle}")
            h,m,s = map(lambda x: (x - angle) % NUM_TICKS, [h,m,s])
            """
            if m % 12 != 0 or s % 720 != 0:
                continue
            """
            actual, pred = get_actual_pred(h,m,s)
            if actual == pred :
                return f"{pred[0]} {pred[1]} {pred[2]} {pred[3]}"

    raise Exception("rip")

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    a,b,c = map(int,input().split())
    res = solution(a,b,c)
    print("Case #{}: {}".format(case_num, res))
