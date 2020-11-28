n = int(raw_input())
arr = map(int, raw_input().split())
gives = {i for i in range(1,n+1)}
needs = {i for i in range(1,n+1)}
edges = dict()

for i, v in enumerate(arr):
    if v != 0:
        edges[i+1] = v
        gives.remove(i+1)
        needs.remove(v)

needs = list(needs)

curr = needs[0]
while len(edges) < n:
    while curr in edges:
        curr = edges[curr]
    next = needs.pop()
    edges[curr] = next
    curr = next

arr = []
for i in range(1, n+1):
    arr.append(str(edges[i]))

print " ".join(arr)
