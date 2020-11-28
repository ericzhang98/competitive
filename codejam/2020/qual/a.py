import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution(*args):
    M, = args

    trace = 0
    for i in range(N):
        trace += M[i][i]

    reprows = 0
    for i in range(N):
        s = set()
        for j in range(N):
            if M[i][j] in s:
                reprows += 1
                break
            s.add(M[i][j])
    
    repcols = 0
    for j in range(N):
        s = set()
        for i in range(N):
            if M[i][j] in s:
                repcols += 1
                break
            s.add(M[i][j])

    return trace, reprows, repcols

T = int(input()) # read num test cases
for case_num in range(1, T + 1):

    N = int(input())
    M = []
    for i in range(N):
       M.append(list(map(int, input().split(" ")))) 

    res = solution(M)
    print("Case #{}: {} {} {}".format(case_num, *res))
