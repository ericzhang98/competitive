import sys
import itertools
import copy
import heapq
import bisect
from collections import defaultdict, Counter


s = raw_input()
per = "PER"*(len(s)/3)
print sum([0 if s[i] == per[i] else 1 for i in range(len(s))])
