n = int(raw_input())
arr = map(int, raw_input().split())

houses = set(arr)
use = set()
for x in sorted(list(houses)):
    if x in use:
        continue
    elif x-1 in use:
        continue
    else:
        use.add(x+1)

mi = len(use)

use = set()
import collections
cnts = collections.Counter(arr)
for x in sorted(list(houses)):
    if x-1 not in use:
        use.add(x-1)
        cnts[x] -= 1
    if x not in use and cnts[x] > 0:
        use.add(x)
        cnts[x] -= 1
    if cnts[x] > 0:
        use.add(x+1)
        cnts[x] -= 1

ma = len(use)

print mi, ma
