from __future__ import print_function
import sys
import math
from collections import defaultdict
import itertools

def twopath(r,c):
    path = []
    top = r
    bot = r+1
    for i in range(3, c+1):
        path.append((bot, i))
        path.append((top, i-2))
    path.append((bot,1))
    path.append((top,c))
    path.append((bot,2))
    path.append((top,c-1))
    return path

def threepath(r,c):
    path = []
    top = r
    mid = r+1
    bot = r+2
    for i in range(3, c+1):
        path.append((mid,i))
        path.append((top,i-2))
        path.append((bot,i-1))
    path.append((top,c))
    path.append((mid,1))
    path.append((bot,c))
    path.append((mid,2))
    path.append((top,c-1))
    path.append((bot,1))
    return path

def path_to_str(path):
    s = ""
    for p in path:
        s += "\n%d %d" % (p[0], p[1])
    return s

def solution(args):
    r = int(args[0][0])
    c = int(args[0][1])

    if r == 1 or c == 1:
        return "IMPOSSIBLE"
    if (r == 2 and c <= 4) or (r <= 4 and c == 2):
        return "IMPOSSIBLE"

    if c >= 5:
        path = []
        if r % 2 == 0:
            for row in range(1,r,2):
                path.extend(twopath(row,c))
        else:
            for row in range(1,r-2,2):
                path.extend(twopath(row,c))
            path.extend(threepath(r-2,c))
        return "POSSIBLE" + path_to_str(path)
    
    if r >= 5:
        temp = r
        r = c
        c = temp
        path = []
        if r % 2 == 0:
            for row in range(1,r,2):
                path.extend(twopath(row,c))
        else:
            for row in range(1,r-2,2):
                path.extend(twopath(row,c))
            path.extend(threepath(r-2,c))
        return "POSSIBLE" + path_to_str(map(lambda (x,y): (y,x), path))

    if r == 3 and c == 4:
        three_by_four = [(2,3),(1,1),(3,2),(2,4),(1,2),(3,1),(1,4),(3,3),(2,1),(1,3),(3,4),(2,2)]
        return "POSSIBLE" + path_to_str(three_by_four)
    if r == 4 and c == 3:
        three_by_four = [(2,3),(1,1),(3,2),(2,4),(1,2),(3,1),(1,4),(3,3),(2,1),(1,3),(3,4),(2,2)]
        return "POSSIBLE" + path_to_str(map(lambda (x,y): (y,x), three_by_four))

    if r == 4 and c == 4:
        four_by_four = [(2,2),(4,3),(2,4),(3,2),(1,3),(2,1),(4,2),(2,3),(1,1),(3,4),(4,1),(1,2),(4,4),(3,1),(1,4),(3,3)]
        return "POSSIBLE" + path_to_str(four_by_four)

    return "IMPOSSIBLE"

t = int(raw_input()) # read a line with a single integer
for case_num in xrange(1, t + 1):

    params = []

    # parsing
    line = raw_input()
    params.append(line.split(" "))

    res = solution(params)
    print("Case #{}: {}".format(case_num, res))
