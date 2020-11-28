import sys
import collections
import heapq
import itertools
import bisect

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution(D, A):
    if D == 2:
        if len(set(A)) == len(A): return 1
        else: return 0
    if D == 3:
        cnts = collections.Counter(A)
        sizes = sorted(cnts.keys())
        most_common = cnts.most_common()
        best = 0
        if most_common[0][1] >= 3: return 0
        for s in sizes:
            if s % 2 == 0 and s // 2 in cnts:
                return 1
            if best == 2:
                return 1
            best = max(best, cnts[s])
        return 2

    A = sorted(A)

        
    return 0

T = int(input()) # read num test cases
for case_num in range(1, T + 1):

    arr = input().split(" ")
    N, D = int(arr[0]), int(arr[1])
    A = list(map(int, input().split(" ")))

    res = solution(D, A)
    print("Case #{}: {}".format(case_num, res))
