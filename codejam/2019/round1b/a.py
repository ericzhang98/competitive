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

def solution(Q, people):
    v = {0: 0, Q+1: 0}
    h = {0: 0, Q+1: 0}
    for x, y, d in people:
        if d == 'N' or d == 'S':
            if d == 'N':
                if y == Q: continue
                if y+1 not in v:
                    max_lt = max(k for k in v if k < y+1)
                    v[y+1] = v[max_lt]
                for k in [k for k in v if k >= y+1]:
                    v[k] += 1
            else:
                if y == 0: continue
                if y not in v:
                    max_lt = max(k for k in v if k < y)
                    v[y] = v[max_lt]
                for k in [k for k in v if k < y]:
                    v[k] += 1
        else:
            if d == 'E':
                if x == Q: continue
                if x+1 not in h:
                    max_lt = max(k for k in h if k < x+1)
                    h[x+1] = h[max_lt]
                for k in [k for k in h if k >= x+1]:
                    h[k] += 1
            else:
                if x == 0: continue
                if x not in h:
                    max_lt = max(k for k in h if k < x)
                    h[x] = h[max_lt]
                for k in [k for k in h if k < x]:
                    h[k] += 1

    maxamt, best = 0, (float('inf'), float('inf'))

    for vk, vamt in v.items():
        for hk, hamt in h.items():
            if vk == Q+1 or hk == Q+1: continue
            candamt, cand = vamt+hamt, (hk,vk)
            if candamt >= maxamt:
                if candamt > maxamt or cand < best:
                    maxamt, best = candamt, cand

    return f"{best[0]} {best[1]}"

def solution_wrong_problem(Q, people):
    v = collections.defaultdict(lambda: {0: 0, Q+1: 0})
    h = collections.defaultdict(lambda: {0: 0, Q+1: 0})
    for x, y, d in people:
        if d == 'N' or d == 'S':
            segment = v[x]
            if d == 'N':
                if y == Q: continue
                if y+1 not in segment:
                    min_gt = min([k for k in segment.keys() if k > y+1])
                    segment[y+1] = segment[min_gt]
                for k in [k for k in segment.keys() if k > y+1]:
                    segment[k] += 1
            else:
                if y == 0: continue
                if y not in segment:
                    min_gt = min([k for k in segment.keys() if k > y])
                    segment[y] = segment[min_gt]
                for k in [k for k in segment.keys() if 0 < k <= y]:
                    segment[k] += 1
        else:
            segment = h[y]
            if d == 'E':
                if x == Q: continue
                if x not in segment:
                    min_gt = min([k for k in segment.keys() if k > x+1])
                    segment[x+1] = segment[min_gt]
                for k in [k for k in segment.keys() if k > x+1]:
                    segment[k] += 1
            else:
                if x == 0: continue
                if x not in segment:
                    min_gt = min([k for k in segment.keys() if k > x])
                    segment[x] = segment[min_gt]
                for k in [k for k in segment.keys() if 0 < k <= x]:
                    segment[k] += 1

    hdivides = {hk: sorted(hsegment.keys()) for hk, hsegment in h.items()}
    vdivides = {vk: sorted(vsegment.keys()) for vk, vsegment in v.items()}

    ans = [0, (float('inf'), float('inf'))]
    def update(candamt, cand):
        eprint("cand:", candamt, cand)
        maxamt, best = ans
        if candamt >= maxamt:
            if candamt > maxamt:
                ans[0] = candamt
                ans[1] = cand
            else:
                if cand < best:
                    ans[0] = candamt
                    ans[1] = cand

    for vk, vsegment in v.items():
        for hk, hsegment in h.items():
            hdivide = hdivides[hk]
            vdivide = vdivides[vk]
            hborder = hdivide[bisect.bisect_right(hdivide, hk)]
            vborder = vdivide[bisect.bisect_right(vdivide, vk)]
            hamt = hsegment[hborder]
            vamt = vsegment[vborder]
            candamt = hamt+vamt
            cand = (vk, hk)
            update(candamt, cand)

    for vk, vsegment in v.items():
        divides = vdivides[vk]
        for i in range(1, len(divides)):
            candamt, cand = vsegment[divides[i]], (vk,divides[i-1])
            update(candamt, cand)

    for hk, hsegment in h.items():
        divides = hdivides[hk]
        for i in range(1, len(divides)):
            candamt, cand = hsegment[divides[i]], (divides[i-1],hk)
            update(candamt, cand)

    return f"{ans[1][0]} {ans[1][1]}"

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    P, Q = map(int, input().split())
    people = []
    for _ in range(P):
        arr = input().split()
        people.append([int(arr[0]), int(arr[1]), arr[2]])
    res = solution(Q, people)
    print("Case #{}: {}".format(case_num, res))
