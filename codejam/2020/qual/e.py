import sys
import itertools
import collections
import time

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def mat_to_str(mat):
    l = []
    for row in mat:
        l.append(" ".join(map(str,row)))
    return "\n".join(l)

def solution(*args):
    N, K = args

    if (N,K) in soln:
        return "POSSIBLE\n" + soln[(N,K)]
    else:
        return "IMPOSSIBLE"

soln = dict()
def precompute():
    for N in range(2,6):
        seen = collections.defaultdict(set)
        mat = [[0]*N for _ in range(N)]
        def dfs(i):
            if i == N:
                trace = sum(mat[i][i] for i in range(N))
                if (N, trace) not in soln: soln[(N,trace)] = mat_to_str(mat)
                return

            for perm in itertools.permutations(list(range(1,N+1))):
                if all(perm[j] not in seen[j] for j in range(N)):
                    for j in range(N):
                        seen[j].add(perm[j])
                        mat[i][j] = perm[j]
                    dfs(i+1)
                    for j in range(N):
                        seen[j].remove(perm[j])
                        mat[i][j] = 0
        dfs(0)

# precompute()

soln = {(2, 2): '1 2\n2 1', (2, 4): '2 1\n1 2', (3, 6): '1 2 3\n2 3 1\n3 1 2', (3, 3): '1 2 3\n3 1 2\n2 3 1', (3, 9): '3 1 2\n2 3 1\n1 2 3', (4, 4): '1 2 3 4\n2 1 4 3\n3 4 1 2\n4 3 2 1', (4, 6): '1 2 3 4\n2 1 4 3\n3 4 2 1\n4 3 1 2', (4, 8): '1 2 3 4\n2 3 4 1\n3 4 1 2\n4 1 2 3', (4, 10): '1 2 3 4\n2 4 1 3\n3 1 4 2\n4 3 2 1', (4, 9): '1 2 3 4\n2 4 1 3\n4 3 2 1\n3 1 4 2', (4, 7): '1 2 3 4\n3 1 4 2\n4 3 2 1\n2 4 1 3', (4, 12): '1 2 3 4\n3 4 1 2\n2 3 4 1\n4 1 2 3', (4, 11): '1 2 3 4\n3 4 2 1\n2 1 4 3\n4 3 1 2', (4, 13): '2 1 3 4\n3 4 2 1\n1 3 4 2\n4 2 1 3', (4, 14): '3 1 2 4\n1 4 3 2\n2 3 4 1\n4 2 1 3', (4, 16): '4 1 2 3\n1 4 3 2\n2 3 4 1\n3 2 1 4', (5, 14): '1 2 3 4 5\n2 1 4 5 3\n3 4 5 1 2\n4 5 2 3 1\n5 3 1 2 4', (5, 10): '1 2 3 4 5\n2 1 4 5 3\n3 4 5 1 2\n5 3 1 2 4\n4 5 2 3 1', (5, 5): '1 2 3 4 5\n2 1 4 5 3\n3 5 1 2 4\n4 3 5 1 2\n5 4 2 3 1', (5, 8): '1 2 3 4 5\n2 1 4 5 3\n3 5 1 2 4\n5 4 2 3 1\n4 3 5 1 2', (5, 9): '1 2 3 4 5\n2 1 4 5 3\n4 5 1 3 2\n3 4 5 2 1\n5 3 2 1 4', (5, 15): '1 2 3 4 5\n2 3 1 5 4\n3 4 5 1 2\n4 5 2 3 1\n5 1 4 2 3', (5, 12): '1 2 3 4 5\n2 3 1 5 4\n3 4 5 1 2\n5 1 4 2 3\n4 5 2 3 1', (5, 11): '1 2 3 4 5\n2 3 1 5 4\n3 5 4 1 2\n4 1 5 2 3\n5 4 2 3 1', (5, 13): '1 2 3 4 5\n2 3 1 5 4\n5 1 4 2 3\n4 5 2 3 1\n3 4 5 1 2', (5, 16): '1 2 3 4 5\n2 3 4 5 1\n4 1 5 2 3\n5 4 1 3 2\n3 5 2 1 4', (5, 17): '1 2 3 4 5\n2 4 1 5 3\n4 3 5 2 1\n5 1 4 3 2\n3 5 2 1 4', (5, 18): '1 2 3 4 5\n2 4 5 1 3\n3 5 4 2 1\n4 3 1 5 2\n5 1 2 3 4', (5, 19): '1 2 3 4 5\n2 5 1 3 4\n3 4 5 1 2\n4 3 2 5 1\n5 1 4 2 3', (5, 20): '1 2 3 4 5\n2 5 4 1 3\n3 4 5 2 1\n4 3 1 5 2\n5 1 2 3 4', (5, 7): '1 2 3 4 5\n3 1 4 5 2\n4 5 2 1 3\n5 3 1 2 4\n2 4 5 3 1', (5, 21): '2 1 3 4 5\n1 5 4 2 3\n3 4 5 1 2\n4 3 2 5 1\n5 2 1 3 4', (5, 22): '3 1 2 4 5\n1 5 4 2 3\n2 4 5 3 1\n4 3 1 5 2\n5 2 3 1 4', (5, 23): '4 1 2 3 5\n1 5 3 4 2\n2 4 5 1 3\n3 2 4 5 1\n5 3 1 2 4', (5, 25): '5 1 2 3 4\n1 5 3 4 2\n2 4 5 1 3\n3 2 4 5 1\n4 3 1 2 5'}


T = int(input()) # read num test cases
for case_num in range(1, T + 1):

    N, K = map(int, input().split(" "))

    res = solution(N, K)
    print("Case #{}: {}".format(case_num, res))
