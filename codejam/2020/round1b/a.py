import sys
import copy
import operator
import math
import collections
import heapq
import itertools
import functools
import bisect

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution(X, Y):
    x,y = X,Y
    if (x+y) % 2 == 0:
        return "IMPOSSIBLE"
    ans = []
    hm = {
        (1,0): 'E',
        (-1,0): 'W',
        (0,1): 'N',
        (0,-1): 'S',
        (0,0): '',
    }
    while (x,y) not in hm:
        eprint(x,y)
        if x % 2 == 1:
            if ((y // 2) + ((x+1) // 2)) % 2 == 1:
                dx,dy = -1,0
            else:
                dx,dy = 1,0
        else:
            if (((y+1) // 2) + (x // 2)) % 2 == 1:
                dx,dy = 0,-1
            else:
                dx,dy = 0,1
        ans.append(hm[(dx,dy)])
        eprint(dx,dy, ans)
        x,y = x-dx, y-dy
        x,y = x//2, y//2
            
    if (x,y) in hm:
        ans.append(hm[(x,y)])
    return "".join(ans)

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    X, Y = map(int, input().split())
    res = solution(X, Y)
    print("Case #{}: {}".format(case_num, res))
