import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution(*args):
    S, = args
    nums = list(map(int, S))
    N = len(nums)

    curr = 0
    par = [""] * (N+1)

    for i, v in enumerate(nums):
        diff = v - curr
        if diff > 0:
            par[i] = "("*diff
        elif diff < 0:
            par[i] = ")"*(-diff)
        curr = v
    par[-1] = ")"*v

    ans = ""
    for i in range(N):
        ans += par[i]
        ans += str(nums[i])
    ans += par[-1]

    return ans

T = int(input()) # read num test cases
for case_num in range(1, T + 1):

    S = input()

    res = solution(S)
    print("Case #{}: {}".format(case_num, res))
