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

def solution(C, D, X, E, UV):
    #print(C, D, X, E, UV)
    ans = {uv: None for uv in UV}
    dist = {i: float('-inf') for i in range(1,C+1)}
    dist[1] = 0

    R = [(X[i-2], i) for i in range(2,C+1) if X[i-2] < 0]
    R.sort()
    R = collections.deque(R)
    T = [(X[i-2], i) for i in range(2,C+1) if X[i-2] > 0]
    T.sort()
    for d, i in T:
        dist[i] = d
    T = collections.deque(T)

    curr_order = 0
    curr_dist = 0
    n = 1
    while len(R) > 0:
        r, i = R[0]
        if r == curr:
            dist[i] = curr_dist
            R.popleft()
            n += 1
            continue

        if -r >= n and len(T) > 0:
            t, j = T[0]
        else:



        curr += 1
        order_dist[curr] = 1 + order_dist[curr-1]
        dist[i] = order_dist[curr]




    """
    q = collections.deque([1])
    curr = 0
    seen = set()
    pos = {i: float('-inf') for i in range(1,C+1)}
    pos[1] = 0
    ordering = collections.defaultdict(list)
    ordering[0].append(1)
    for curr in range(0,-C,-1):
        while len(ordering[curr]) > 0:
            u = ordering[curr].pop()
            if u in seen: continue
            seen.add(u)

            # set distance for u
            # add latencies to edges where neighbor computer already has distance set
            if u != 1:
                Xu = X[u-2]
                if Xu > 0:
                    dist[u] = Xu
                else:
                    # 1 + max of all vertices whose ordering is before it
                    #valid = [v for v in E[u] if pos[v] > Xu]
                    #print(u, E[u], Xu, valid)
                    #print([pos[v] for v in E[u]])
                    if curr not in order_dist:
                        valid = [v for v in range(1,C+1) if pos[v] > Xu]
                        order_dist[curr] = max([dist[v] for v in valid]) + 1
                    dist[u] = order_dist[curr]
                for v in E[u]:
                    if dist[v] != float('-inf'):
                        latency = abs(dist[u] - dist[v])
                        latency = max(latency, 1)
                        ans[tuple(sorted([u,v]))] = latency

            # add neighbors of u to ordering
            for v in E[u]:
                if v not in seen:
                    Xv = X[v-2]
                    if Xv < 0:
                        ordering[Xv].append(v)
                        pos[v] = Xv
                    else:
                        ordering[curr].append(v)
                        #pos[v] = curr
    """

    ansl = [str(ans[uv]) for uv in UV]
    return " ".join(ansl)

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    C, D = list(map(int, input().split()))
    X = list(map(int, input().split()))
    E = collections.defaultdict(list)
    UV = []
    for i in range(D):
        U, V = list(map(int, input().split()))
        E[U].append(V)
        E[V].append(U)
        UV.append((U,V))
    E = dict(E)

    res = solution(C, D, X, E, UV)
    print("Case #{}: {}".format(case_num, res))
