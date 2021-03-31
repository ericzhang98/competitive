import sys
import copy
import operator
import math
import collections
import heapq
import itertools
import functools
import bisect
import numpy as np

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution(data):
    num_correct_i = np.sum(data, axis=1)
    argsort_correct_i = np.argsort(num_correct_i)
    data = data[argsort_correct_i]
    num_correct_j = np.sum(data, axis=0)
    argsort_correct_j = np.flip(np.argsort(num_correct_j))
    data = data[:,argsort_correct_j]

    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    def inv_sigmoid(y):
        return np.log(y / (1 - y))
    num_correct_i = np.sum(data, axis=1)
    num_correct_j = np.sum(data, axis=0)
    expected_skill = inv_sigmoid(num_correct_i/10000)
    expected_difficulty = -inv_sigmoid(num_correct_j/100)

    def expected_correct(skill, difficulties):
        return np.sum(sigmoid(np.full(difficulties.shape, skill) - difficulties))
    n = 1000
    diff = []
    for i in range(100):
        expected_easy = expected_correct(expected_skill[i], expected_difficulty[:n])
        actual_easy = np.sum(data[i][:n])
        expected_hard = expected_correct(expected_skill[i], expected_difficulty[-n:])
        actual_hard = np.sum(data[i][-n:])
        #diff.append((expected_easy - actual_easy) + (actual_hard - expected_hard))
        diff.append(actual_hard-expected_hard)
    diff = np.array(diff)

    ans = argsort_correct_i[np.argsort(diff)[-1]] + 1
    return ans

T = int(input()) # read num test cases
P = int(input())
for case_num in range(1, T + 1):
    answers = []
    for _ in range(100):
        answers.append(list(map(int,list(input()))))
    answers = np.array(answers)
    res = solution(answers)
    print("Case #{}: {}".format(case_num, res))
