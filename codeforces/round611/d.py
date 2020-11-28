n, m = map(int, raw_input().split())
trees = map(int, raw_input().split())

occupied = set(trees)
total = 0
res = []

import collections
q = collections.deque(map(lambda x: (0,x), trees))
while len(occupied) < n+m:
    dist, curr = q.popleft()
    if curr not in occupied:
        occupied.add(curr)
        res.append(curr)
        total += dist
    neigh = [curr-1, curr+1]
    for ne in neigh:
        if ne not in occupied:
            q.append((dist+1, ne))

print total
print " ".join(map(str, res))
