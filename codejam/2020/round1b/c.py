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
    print("--", *args, file=sys.stderr, **kwargs)

def solution(r,s):
    stack = sum([list(range(1,r+1))] * s, [])
    # abc...zabc... -> c...zaabbc... == c...zabc...
    ans = []
    ops = math.ceil((r*s - r) / 2)
    eprint(stack)
    for op in range(ops):
        toptwo = []
        cut1 = None
        for i in range(len(stack)-1):
            j = i+1
            if len(toptwo) != 2:
                if stack[i] not in toptwo:
                    toptwo.append(stack[i])
            else:
                if cut1 is None and stack[i] != toptwo[1]:
                    cut1 = i
                if stack[i] == toptwo[0] and stack[j] == toptwo[1]:
                    ans.append((cut1, i+1-cut1))
                    break
        else:
            eprint('odd case')
            assert(toptwo[0] == r and toptwo[1] == 1 and op == ops-1)
            for i in range(len(stack)):
                if stack[i] != stack[0]:
                    break
            ans.append((i, len(stack)-i))
        x,y = ans[-1]
        eprint(x,y)
        stack = stack[x:x+y] + stack[:x] + stack[x+y:]
        eprint(stack)
    return f"{len(ans)}\n" + "\n".join(f"{x} {y}" for x,y in ans)

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    r, s = map(int, input().split())
    res = solution(r,s)
    print("Case #{}: {}".format(case_num, res))
