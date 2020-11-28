import sys
import itertools
import copy
import heapq
import bisect
from collections import defaultdict, Counter, deque
import re


goblins = []
sprinklers = []

n = int(raw_input())
for _ in range(n):
    goblins.append(raw_input().strip())

n = int(raw_input())
for _ in range(n):
    sprinklers.append(raw_input().strip())

print goblins
print sprinklers

bad = set(itertools.product(range(10001), range(10001)))


for s in sprinkers:
    print s
    x, y, r = map(int, s.split(" "))
    r_sq = r**2
    for x2, y2 in itertools.product(range(x-r, x+r+1), range(y-r, y+r+1)):
        dist_sq = (x-x2)**2 + (y-y2)**2
        if dist_sq <= r_sq:
            print (x2,y2)
            good.remove((x2,y2))

count = 0
for g in goblins:
    x, y = map(int, g.split(" "))
    if (x,y) in good:
        count += 1
