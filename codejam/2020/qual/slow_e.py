import sys
import itertools
import collections

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def matrix_to_str(mat):
    l = []
    for row in mat:
        l.append(" ".join(map(str,row)))
    return "\n".join(l)

def solution(*args):
    N, K = args

    seen = collections.defaultdict(set)
    mat = [[0]*N for _ in range(N)]
    def dfs(i):
        if i == N:
            trace = sum(mat[i][i] for i in range(N))
            return trace == K

        for perm in itertools.permutations(list(range(1,N+1))):
            if all(perm[j] not in seen[j] for j in range(N)):
                for j in range(N):
                    seen[j].add(perm[j])
                    mat[i][j] = perm[j]
                if dfs(i+1): return True
                for j in range(N):
                    seen[j].remove(perm[j])
                    mat[i][j] = 0

    if dfs(0):
        return "POSSIBLE\n" + matrix_to_str(mat)
    else:
        return "IMPOSSIBLE"

T = int(input()) # read num test cases
for case_num in range(1, T + 1):

    N, K = map(int, input().split(" "))

    res = solution(N, K)
    print("Case #{}: {}".format(case_num, res))
