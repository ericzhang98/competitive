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

def solution(nums):
    nums.sort()
    highest = 0
    for i in range(len(nums)):
        if highest < nums[i]:
            highest += 1
    return highest

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    n = input()
    nums = list(map(int,input().split()))
    res = solution(nums)
    print("Case #{}: {}".format(case_num, res))
