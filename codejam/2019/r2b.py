from __future__ import print_function
import sys
import math

def solution(args):
    r_param = int(args[0])
    b_param = int(args[1])
    if r_param > 25 or b_param > 25:
        return 0
    return dp[26*26-1][r_param][b_param]

def matrix(h, w, type=int):
    return [[type() for _ in range(w)] for _ in range(h)]

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# insight: dp on the actual pairs allowed and (b,r) , recursive relationship is max across submatrix

dp = [matrix(26, 26, int) for _ in range(26*26)]
for i in range(1, 26*26):
    prev = dp[i-1]
    next = dp[i]
    new_r = i / 26
    new_b = i % 26
    for r in range(26):
        for b in range(26):
            if r-new_r >= 0 and b-new_b >= 0:
                next[r][b] = max(prev[r][b], prev[r-new_r][b-new_b]+1)
            else:
                next[r][b] = prev[r][b]

print(dp[26*26-1])

t = int(raw_input()) # read a line with a single integer
for case_num in xrange(1, t + 1):
    line = raw_input()

    params = line.split(" ")

    res = solution(params)
    print("Case #{}: {}".format(case_num, res))
