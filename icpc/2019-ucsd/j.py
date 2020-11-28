import sys
import itertools
import copy
import heapq
import bisect
from collections import defaultdict, Counter, deque
import math

class Node:
    def __init__(self, rank, val):
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

outgoing = dict()
incoming = defaultdict(list)

n = int(raw_input())
ids = []
for _ in range(n):
    line = raw_input().strip()
    arr = map(int, line.split(" "))
    ids.append(arr[0])
    outgoing[arr[0]] = arr[2:]
    for o in outgoing[arr[0]]:
        incoming[o].append(arr[0])

trapped = set(outgoing.keys())
reachable = set(outgoing.keys())

q = deque([0])
while len(q) > 0:
    curr = q.popleft()
    print curr
    print incoming[curr]
    trapped.discard(curr)
    for e in incoming[curr]:
        if e in trapped:
            q.append(e)

q = deque([0])
while len(q) > 0:
    curr = q.popleft()
    reachable.discard(curr)
    for e in outgoing[curr]:
        if e not in reachable:
            q.append(e)

if len(trapped) == 0 and len(reachable) == 0:
    print "NO PROBLEMS"
else:
    for id in ids:
        if id in trapped:
            print "TRAPPED", id
    for id in ids:
        if id in reachable:
            print "UNREACHABLE", id
