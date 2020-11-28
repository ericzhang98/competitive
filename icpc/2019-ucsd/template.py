import sys
import itertools
import copy
import heapq
import bisect
from collections import defaultdict, Counter


_ = raw_input()

nums = map(int, raw_input().split(" "))

lt = []
gt = []

a = []
for n in nums:
    num_gt = len(a) - bisect.bisect_right(a, n)
    gt.append(num_gt)
    a.append(n)

a = []
for n in nums[::-1]:
    num_lt = bisect.bisect_left(a,n)
    lt.append(num_lt)
    a.append(n)


print gt
print lt

gt = gt[::-1]

print sum([gt[i]*lt[i] for i in range(len(gt))])


def solve(arr):
    x = 0
    for i, j, k in itertools.combinations(range(len(arr)), 3):
        if arr[i] > arr[j] > arr[k]:
            x += 1
    return x


print solve(nums)
