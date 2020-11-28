import sys
import itertools
import copy
import heapq
import bisect
from collections import defaultdict, Counter, deque
import re

params = []
for line in sys.stdin:
    params.append(line.strip())

files = params[2:]

reg = params[0]
efficient = []
i = 0
while i < len(reg):
    if i > 0 and reg[i] == '*' and reg[i-1] == '*': 
        i += 1
        continue
    efficient.append(reg[i])
    i += 1

reg = "".join(efficient)
reg = reg.replace(".", "0")
reg = reg.replace("*", ".*")
reg = reg.replace("0", "\.")
r = re.compile("^" + reg + "$")

for f in files:
    if r.search(f):
        print f
