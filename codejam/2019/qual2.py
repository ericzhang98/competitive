from __future__ import print_function
import sys
import math
from collections import defaultdict, deque

def solution(args):
    N = int(args[0])
    bad_path = list(args[1])

    asdf = args[1]
    asdf = asdf.replace("S", "A")
    asdf = asdf.replace("E", "S")
    asdf = asdf.replace("A", "E")
    return asdf

    bad_e = dict()
    curr = (0,0)
    for i in range(2*N-2):
        if bad_path[i] == 'S':
            next = (curr[0]+1, curr[1])
        else:
            next = (curr[0], curr[1]+1)
        bad_e[curr] = next
        curr = next

    paths = dict()
    queue = deque()
    paths[(0,0)] = ""
    queue.append((0,0))
    while (N-1,N-1) not in paths:
        curr = queue.popleft()
        s_next = (curr[0]+1, curr[1])
        e_next = (curr[0], curr[1]+1)
        if curr not in bad_e or bad_e[curr] != s_next:
            if s_next not in paths:
                paths[s_next] = paths[curr] + "S"
                queue.append(s_next)
        if curr not in bad_e or bad_e[curr] != e_next:
            if e_next not in paths:
                paths[e_next] = paths[curr] + "E"
                queue.append(e_next)
        del paths[curr]


    return paths[(N-1,N-1)]

def matrix(height, width, type=int):
    return [[type() for _ in range(w)] for _ in range(h)]

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

t = int(raw_input()) # read a line with a single integer
for case_num in xrange(1, t + 1):
    line = raw_input()
    another_line = raw_input()

    params = []
    params.append(line)
    params.append(another_line)

    res = solution(params)
    print("Case #{}: {}".format(case_num, res))
