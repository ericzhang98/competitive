from __future__ import print_function
input = raw_input
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

def bellman_ford(graph, costs, V, source, sink):
    dist = collections.defaultdict(lambda: float('inf'))
    prv = {}
    dist[source] = 0
    # relaxation -- min-cost k-length path at each kth iteration 
    for _ in range(V-1):
        for u in graph:
            for v in graph[u]:
                if graph[u][v] > 0:
                    if dist[u] + costs[u][v] < dist[v]:
                        dist[v] = dist[u] + costs[u][v]
                        prv[v] = u
    # negative cycles can occur, but thats ok, so don't check
    if dist[sink] == float('inf'):
        return False, [] # sink unreachable
    path = collections.deque()
    v = sink
    while v != source:
        path.appendleft((prv[v], v))
        v = prv[v]
    return True, path

# only works on flow networks with single directional flows
# make sure graph and cost are collections.defaultdict(lambda: collections.defaultdict(int))
# graph[u][v] = capacity of edge
# costs[u][v] = cost per unit flow
# edits the graph by maintaining it as residual graph
def min_cost_flow(graph, costs, source, sink, desired_flow=float('inf')):
    pairs = []
    for u in list(costs):
        for v in list(costs[u]):
            costs[v][u] = -costs[u][v]
    min_cost = 0
    curr_flow = 0
    # augment the flow while less than desired flow by pushing flow from 
    while curr_flow < desired_flow:
        residual_flow_exists, residual_path = bellman_ford(graph, costs, len(costs), source, sink)
        if not residual_flow_exists:
            return curr_flow, min_cost
        residual_capacity = min(graph[u][v] for u, v in residual_path)
        residual_capacity = min(residual_capacity, desired_flow - curr_flow) # upper bound additional flow by remaining delta before desired flow
        curr_flow += residual_capacity
        # update residual graph and min_cost
        for u, v in residual_path:
            graph[u][v] -= residual_capacity
            graph[v][u] += residual_capacity
            min_cost += residual_capacity * costs[u][v]
    return curr_flow, min_cost

# edges must be a dict mapping vertex -> [neighbors] -> cost
# left and right are lists of the 2 disjoint sets
def min_cost_bipartite_matching(edges, left, right):
    source, sink = "source", "sink"
    graph = collections.defaultdict(lambda: collections.defaultdict(int))
    costs = collections.defaultdict(lambda: collections.defaultdict(int))
    for u in left:
        graph[source][u] = 1
        costs[source][u] = 0
    for v in right:
        graph[v][sink] = 1
        costs[v][sink] = 0
    for u in left:
        for v in edges[u]:
            graph[u][v] = 1
            costs[u][v] = edges[u][v]
    return min_cost_flow(graph, costs, source, sink)

def solution(curr, desired, F, C):
    R, C = len(curr), len(curr[0])
    total_cost = 0
    m_to_g = []
    g_to_m = []
    for i in range(R):
        for j in range(C):
            if curr[i][j] == 0 and desired[i][j] == 1:
                m_to_g.append((i,j))
            if curr[i][j] == 1 and desired[i][j] == 0:
                g_to_m.append((i,j))
    must_flip = abs(len(m_to_g) - len(g_to_m))
    total_cost += must_flip * F
    edges = collections.defaultdict(lambda: collections.defaultdict(int))
    for x0,y0 in m_to_g:
        for x1,y1 in g_to_m:
            swap_cost = (abs(x0-x1) + abs(y0-y1)) * S # L1 distance number of swaps
            flip_cost = 2*F
            cost = min(swap_cost, flip_cost)
            edges[(x0,y0)][(x1,y1)] = cost
    max_matching, min_cost = min_cost_bipartite_matching(edges, m_to_g, g_to_m)
    total_cost += min_cost
    return total_cost

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    R,C,F,S = map(int,input().split())
    curr = []
    for _ in range(R):
        curr.append([1 if c == 'G' else 0 for c in list(input())])
    desired = []
    for _ in range(R):
        desired.append([1 if c == 'G' else 0 for c in list(input())])
    res = solution(curr, desired, F, S)
    print("Case #{}: {}".format(case_num, res))
