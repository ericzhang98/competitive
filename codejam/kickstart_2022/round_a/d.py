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

@functools.lru_cache(None)
def dp(n, total_product, total_sum):
    if n == 0:
        if total_sum == 0: return 0
        return 1 if total_product % total_sum == 0 else 0
    count = 0
    for digit in range(0, 10):
        subcount = dp(n-1, total_product * digit, total_sum + digit)
        count += subcount
    return count

def count_for_length(n):
    if n == 0: return 0
    count = 0
    for digit in range(1, 10):
        subcount = dp(n-1, digit, digit)
        count += subcount
    return count

def total_count(x):
    if x == 0: return 0
    s = list(str(x))
    n = len(s)
    count = 0
    for idx in range(n):
        subcount = count_for_length(n-idx-1)
        count += subcount
        for digit in range(1 if idx == 0 else 0, int(s[idx]) if idx < n-1 else int(s[idx])+1):
            prefix = s[:idx] + [str(digit)]
            prefix_product = functools.reduce(lambda x,y: x*y, map(int, prefix), 1)
            prefix_sum = sum(map(int, prefix))
            subcount = dp(n-idx-1, prefix_product, prefix_sum)
            count += subcount
    return count

def solution(A, B):
    ans = total_count(B) - total_count(A-1)
    return ans

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    A, B = map(int, input().split())
    res = solution(A, B)
    print("Case #{}: {}".format(case_num, res))

# # have to rebuild each time so it's too slow
# def total_count(x):
#     if x == 0: return 0
#     s = list(str(x))
#     n = len(s)
#     @functools.lru_cache(None)
#     def dp(digit_place, is_capped, zero_allowed, total_product, total_sum):
#         if digit_place == n:
#             if total_sum == 0: return 0
#             return 1 if total_product % total_sum == 0 else 0
#         count = 0
#         cap = 9 if not is_capped else int(s[digit_place])
#         for digit in range(0, cap+1):
#             nxt_digit_place = digit_place + 1
#             nxt_is_capped = is_capped and digit == cap
#             if digit == 0 and not zero_allowed:
#                 nxt_zero_allowed = False
#                 nxt_product = total_product
#                 nxt_sum = total_sum
#             else:
#                 nxt_zero_allowed = True
#                 nxt_product = total_product * digit
#                 nxt_sum = total_sum + digit
#             subcount = dp(nxt_digit_place, nxt_is_capped, nxt_zero_allowed, nxt_product, nxt_sum)
#             count += subcount
#         return count
#     return dp(0, True, False, 1, 0)
