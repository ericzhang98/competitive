import sys
import itertools
import copy
import heapq
import bisect
from collections import defaultdict, Counter, deque


n, m = map(int, raw_input().split(" "))

arr = []

for i in range(n):
    arr.append(map(int, [c for c in raw_input()]))

dp = [[0 for _ in range(m)] for _ in range(n)]

dp[0][0] = 0

visited = set()
q = deque()
q.append((0,0,0))
res = -1
while len(q) > 0:
    i, j, dist = q.popleft()
    visit = i, j
    if visit in visited: continue
    visited.add(visit)
    if visit == (n-1,m-1): 
        res = dist
        break
    k = arr[i][j]
    for x,y in [(i+k,j), (i-k,j), (i,j+k), (i,j-k)]:
        if 0 <= x < n and 0 <= y < m:
            q.append((x,y,dist+1))

print res
