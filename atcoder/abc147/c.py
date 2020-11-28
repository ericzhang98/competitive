# -*- coding: utf-8 -*-
N = int(raw_input())
A = []
B = []
for n in range(N):
    A_i = int(raw_input())
    honest_i = set()
    unkind_i = set()
    for i in range(A_i):
        x, y =  map(int, raw_input().split())
        if y == 0:
            unkind_i.add(x-1)
        else:
            honest_i.add(x-1)
    A.append(unkind_i)
    B.append(honest_i)

def check(cand, A, B):
    honest = {i for i,v in enumerate(cand) if v == 1}
    unkind = {i for i,v in enumerate(cand) if v == 0}
    for h in honest:
        if len(honest.intersection(A[h])) != 0:
            return False
        if len(unkind.intersection(B[h])) != 0:
            return False
    return True

best = 0
import itertools
for cand in itertools.product([0,1], repeat=N):
    if check(cand, A, B):
        count = cand.count(1)
        best = max(best, count)

print best
