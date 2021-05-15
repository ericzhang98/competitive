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

def solution(K, P):
    P = list(sorted(P))
    segments = []
    curr = 1
    N = len(P)
    for p in P:
        left = curr
        right = p-1
        if left <= right:
            segment = (left, right)
            segments.append(segment)
        curr = p+1
    left = curr
    right = K
    if left <= right:
        segment = (left, right)
        segments.append(segment)

    #eprint(segments)

    if len(segments) == 0:
        return float(0) 
    if len(segments) == 1:
        l, r = segments[0]
        return float(r-l+1) / K

    double_scores = []
    for segment in segments:
        l, r = segment
        double_scores.append(r-l+1)
    double_cand = max(double_scores)

    single_scores = []
    if segments[0][0] == 1:
        single_scores.append(segments[0][1] - segments[0][0] + 1)
        segments.pop(0)
    if segments[-1][1] == K:
        single_scores.append(segments[-1][1] - segments[-1][0] + 1)
        segments.pop()
    for segment in segments:
        l, r = segment
        single_scores.append((r-l+1+1)//2)
    single_scores = list(sorted(single_scores))
    single_cand = single_scores[-1] + single_scores[-2]

    # eprint(single_scores, double_scores, single_cand, double_cand)

    ans = max(single_cand, double_cand)
    return float(ans) / K

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    N, K = map(int, input().split())
    P = map(int, input().split())
    res = solution(K, P)
    print("Case #{}: {}".format(case_num, res))
