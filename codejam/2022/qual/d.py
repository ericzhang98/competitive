import sys
import copy
import operator
import math
import collections
import heapq
import itertools
import functools
import bisect

sys.setrecursionlimit(1000000000)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution(fun, point):
    n = len(fun)
    # each dag is independent
    # have to use last node 
    edges = collections.defaultdict(list)
    roots = []
    for i, p in enumerate(point):
        # i+1 -> p, abyss if p == 0
        # store reverse edges
        edges[p].append(i+1)
        if p == 0:
            roots.append(i+1)
    all_leaves = []
    # print(edges)
    for k in range(1, n+1):
        if k not in edges:
            all_leaves.append(k)
    # minchild is min(minchild(x) for x in children) with value (minchild value, cur value)
    @functools.lru_cache(None)
    def min_child(cur):
        if len(edges[cur]) == 0:
            return fun[cur-1], cur
        min_child_fun, min_child_id = float('inf'), None
        for nxt in edges[cur]:
            cand_fun, _ = min_child(nxt)
            if cand_fun < min_child_fun:
                min_child_fun = cand_fun
                min_child_id = nxt
        return max(fun[cur-1], min_child_fun), min_child_id
    # choose a path to leaf node, separate out into different sub problems
    # always choose minchild when deciding path to leaf node
    def pick_path(cur):
        if len(edges[cur]) == 0:
            return fun[cur-1], cur
        best_fun, best_id = float('inf'), None
        for nxt in edges[cur]:
            cand_fun, _ = min_child(nxt)
            if cand_fun < best_fun:
                best_fun = cand_fun
                best_id = nxt
        # print(cur, best_id)
        for nxt in edges[cur]:
            if nxt != best_id:
                roots.append(nxt)
        path_fun, leaf = pick_path(best_id)
        return max(fun[cur-1], path_fun), leaf

    ans = 0
    leaves = []
    while roots:
        # print(roots)
        cur = roots.pop()
        path_fun, leaf = pick_path(cur)
        ans += path_fun
        leaves.append(leaf)
    # print(leaves, all_leaves)
    assert len(leaves) == len(all_leaves)
    assert set(leaves) == set(all_leaves)
    return ans

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    n = input()
    fun = list(map(int,input().split()))
    point = list(map(int,input().split()))
    res = solution(fun, point)
    print("Case #{}: {}".format(case_num, res))
