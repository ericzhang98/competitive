from __future__ import print_function
import sys
import math
from collections import defaultdict
import heapq

def solution(args):
    n = args[0]
    k = args[1]
    c = args[2]
    d = args[3]

    cheap_min = []
    dheap_min= []
    cheap_max = []
    dheap_max= []
    
    res = 0
    for i in range(n):
        heapq.heappush(cheap_max, c[n])
        heapq.heappush(cheap_max, -c[n])
        heapq.heappush(dheap_max, d[n])
        heapq.heappush(dheap_max, -d[n])

    return 0

def matrix(height, width, type=int):
    return [[type() for _ in range(w)] for _ in range(h)]

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

t = int(raw_input()) # read a line with a single integer
for case_num in xrange(1, t + 1):

    params = []

    # parsing
    line = raw_input()
    arr = line.split()
    n = int(arr[0])
    k = int(arr[1])
    params.append(n)
    params.append(k)
    line = raw_input()
    arr = map(int, line.split())
    params.append(arr)
    line = raw_input()
    arr = map(int, line.split())
    params.append(arr)

    res = solution(params)
    print("Case #{}: {}".format(case_num, res))
