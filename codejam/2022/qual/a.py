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

def solution(a,b):
    ans = []
    line1 = ['+']*(2*b+1)
    for i in range(1,2*b,2):
        line1[i] = '-'
    line2 = ['|']*(2*b+1)
    for i in range(1,2*b,2):
        line2[i] = '.'
    for i in range(a):
        ans.append(copy.copy(line1))
        ans.append(copy.copy(line2))
    ans.append(copy.copy(line1))
    ans[0][0] = '.'
    ans[0][1] = '.'
    ans[1][0] = '.'
    s = "\n" + "\n".join("".join(row) for row in ans)
    return s

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    a, b = list(map(int,input().split()))
    res = solution(a,b)
    print("Case #{}: {}".format(case_num, res))
