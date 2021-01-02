import sys
import math
from collections import defaultdict

def solution(args):
    words = args[0]
    suffixes = defaultdict(int)
    suffix_len = defaultdict(set)
    for w in list(words):
        suffixes[w] = 1
        suffix_len[len(w)].add(w)

    res = 0
    for l in range(max(suffix_len.keys()),0,-1):
        suffix_set = suffix_len[l]
        for c in list(suffix_set):
            if suffixes[c] >= 2:
                res += 2
                suffixes[c[1:]] += (suffixes[c] - 2)
                suffix_len[len(c[1:])].add(c[1:])
            else:
                suffixes[c[1:]] += suffixes[c]
                suffix_len[len(c[1:])].add(c[1:])

    return res

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

t = int(input()) # read a line with a single integer
for case_num in range(1, t + 1):

    params = []

    # parsing
    num = int(input())
    words = set()
    for n in range(num):
        word = input()
        words.add(word)

    params.append(words)

    res = solution(params)
    print("Case #{}: {}".format(case_num, res))
