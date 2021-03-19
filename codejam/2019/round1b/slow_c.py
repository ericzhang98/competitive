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

def solution(N,O,C,D):
    K = int(math.ceil(math.log(N+1,2)))
    RMQC = [[0 for _ in range(K)] for _ in range(N)]
    RMQD = [[0 for _ in range(K)] for _ in range(N)]
    for i in range(N):
        RMQC[i][0] = C[i]
        RMQD[i][0] = D[i]
    for k in range(1, K):
        for i in range(0, N-2**k+1):
            RMQC[i][k] = max(RMQC[i][k-1], RMQC[i+2**(k-1)][k-1])
            RMQD[i][k] = max(RMQD[i][k-1], RMQD[i+2**(k-1)][k-1])
    
    def rmquery(RMQ, i, j):
        length = j-i
        if length == 0: return float('-inf')
        k = int(math.floor(math.log(length,2)))
        left = RMQ[i][k]
        right = RMQ[j-2**k][k]
        return max(left, right)

    def subsolve(i):
        # Li, Ri limits where max([C[Li]..C[Ri-1]]) == C[i]
        Li = i
        for j in range(i-1,-1,-1):
            if max(C[j:i]) >= C[i]:
                break
            else:
                Li = j
        Ri = i
        for j in range(i+1,N+1):
            if max(C[i:j]) > C[i]:
                break
            else:
                Ri = j

        # Ai, Bi limits where max([D[Ai]..D[Bi-1]]) <= C[i] + O
        Ai = i
        for j in range(i-1,Li-1,-1):
            if max(D[j:i+1]) > C[i] + O:
                break
            else:
                Ai = j
        Bi = i
        for j in range(i+1,Ri+1):
            if max(D[i:j]) > C[i] + O:
                break
            else:
                Bi = j

        # Xi, Yi limits where max([D[Xi]..D[Yi-1]]) <= C[i] - O
        Xi = i
        for j in range(i-1,Li-1,-1):
            if max(D[j:i+1]) >= C[i] - O:
                break
            else:
                Xi = j
        Yi = i
        for j in range(i+1,Ri+1):
            if max(D[i:j]) >= C[i] - O:
                break
            else:
                Yi = j

        a = (i+1 - Ai) * (Bi - i)
        b = (i+1 - Xi) * (Yi - i)
        ans = a - b

        eprint(f"--i={i},Li={Li},Ri={Ri},Ai={Ai},Bi={Bi},Xi={Xi},Yi={Yi},a={a},b={b},ans={ans}")

        return ans

    ans = 0
    for i in range(N):
        ans += subsolve(i)
    return ans

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    N, O = map(int, input().split())
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    res = solution(N, O, C, D)
    print("Case #{}: {}".format(case_num, res))

