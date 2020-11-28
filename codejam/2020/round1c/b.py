import sys
import collections
import heapq
import itertools
import bisect

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution(U, L):
    ans = []
    chars = set()
    used = set()
    cnts = collections.Counter()
    cnts_pos = collections.defaultdict(lambda: collections.Counter())
    left_cnts = collections.Counter()
    for Q, R in L:
        """
        for i, c in enumerate(reversed(list(R))):
            cnts_pos[U-1-i][c] += 1
        """
        left_cnts[R[0]] += 1
        for c in list(R):
            cnts[c] += 1
    chars = set(cnts.keys())
    possible_zero = set(chars)
    for Q, R in L:
        possible_zero.discard(R[0])
    zero = list(possible_zero)[0]
    used.add(zero)

    """
    most_common = cnts.most_common()
    wtf = []
    wtf.append(most_common[-1][0])
    for c, cnt in most_common[:-1]:
        wtf.append(c)

    for i in range(U):
        most_common = cnts_pos[i].most_common()
        if len(most_common) == 0: continue
        for c, cnt in most_common:
            if cnt < 100: break
            if c not in used:
                ans.append(c)
                used.add(c)
    """

    ans.append(zero)
    most_common = left_cnts.most_common()
    for c, cnt in most_common:
        ans.append(c)

    return "".join(ans)

T = int(input()) # read num test cases
for case_num in range(1, T + 1):

    U = int(input())
    L = []
    for _ in range(10**4):
        arr = input().split(" ")
        L.append((int(arr[0]), arr[1]))

    res = solution(U, L)
    print("Case #{}: {}".format(case_num, res))
