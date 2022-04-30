import sys
import copy
import operator
import math
import collections
import heapq
import itertools
import functools
import bisect
import random

sys.setrecursionlimit(1000000000)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def easy_solution():
    stack = []
    print('00000000')
    while True:
        inp = int(input())
        if inp == 0:
            return
        if inp == -1:
            return
        n = inp
        stack.append(n)
        if n == 8:
            print('11111111')
        elif n == 4:
            if len(stack) >= 2 and stack[-1] == 4 and stack[-2] == 4:
                print('10000000')
            else:
                print('11110000')
        elif n == 6:
            print('11000000')
        elif n == 2:
            print('11000000')
        elif n == 7:
            print('10000000')
        elif n == 1:
            print('10000000')
        elif n == 3:
            print('10000000')
        elif n == 5:
            print('10000000')

def hard_solution():
    def P(n):
        if n == 0:
            return ['1']
        if n == 1:
            return ['11', '10', '11']
        # - L xor R xor S xor S = L xor R
        # - if we do L+R xor (S interlaced with 0), then the resulting left xor right = L xor R xor S
        # induction is as follows
        # assume we have P(n-1) sequence that makes any 2^(n-1) bit sequence all 0's at some point in the sequence
        # we have a 2^n bit sequence with 2 2^(n-1) halves L, R
        # applying the expanded P(n-1)+P(n-1) sequence does not change the value of L xor R
        # if L = R (i.e. L xor R = all 0), then applying the expanded P(n-1)+P(n-1) sequence results in all 0's at some point in the sequence
        # regardless of L, R, applying P(n-1) interlaced with 0 results in L xor R = all 0 (i.e. L = R) at some point in the sequence
        guaranteed_sequence = P(n-1)
        zero_check_sequence = [s+s for s in guaranteed_sequence]
        make_lr_equal_sequence = [s+'0'*len(s) for s in guaranteed_sequence]
        res = copy.copy(zero_check_sequence)
        for subsequence in make_lr_equal_sequence:
            res += [subsequence]
            res += copy.copy(zero_check_sequence)
        return res
    guaranteed_sequence = collections.deque(P(3))
    while True:
        nxt = guaranteed_sequence.popleft()
        print(nxt)
        inp = int(input())
        if inp == 0:
            return
        if inp == -1:
            return

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    hard_solution()
