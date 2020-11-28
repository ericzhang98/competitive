import sys
import itertools
import copy
import heapq
import bisect
from collections import defaultdict, Counter, deque
import math

MOD = 2**31 - 1

class Node:
    def __init__(self, root, rank, val):
        self.parent = self
        self.rank = rank
        self.val = val

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root.rank > b_root.rank:
        b_root.parent = a_root
    elif a_root.rank < b_root.rank:
        a_root.parent = b_root
    elif a_root != b_root:
        b_root.parent = a_root
        a_root.rank += 1

def find(a):
    if a.parent == a:
        return a
    else:
        a.parent = find(a.parent)
        return a.parent

arr = []
params = []
n = int(raw_input())
for _ in range(n):
    line = raw_input().strip()
    arr.append([c for c in line])

m, n = len(arr[0]), len(arr)

prev_dp = [0 for _ in range(m)]
curr_dp = [0 for _ in range(m)]
curr_dp[0] = 1

prev = []
curr = []

for i in range(n):
    for j in range(m):
        node = Node(None, 0, (i,j))
        curr.append(node)
        if i == 0 and j == 0:
            start = node
            continue
        if arr[i][j] == '#': 
            continue
        paths = 0
        if i > 0:
            paths += prev_dp[j]
            if arr[i-1][j] != '#':
                union(node, prev[j])
        if j > 0:
            paths += curr_dp[j-1]
            if arr[i][j-1] != '#':
                union(node, curr[-2])
        curr_dp[j] = paths % MOD
    prev = curr
    curr = []
    prev_dp = curr_dp
    curr_dp = [0 for _ in range(m)]


if prev_dp[-1] > 0:
    print prev_dp[-1] % MOD
else:
    
    reachable = find(start) == find(prev[-1])

    if reachable:
        print "THE GAME IS A LIE"
    else:
        print "INCONCEIVABLE"
