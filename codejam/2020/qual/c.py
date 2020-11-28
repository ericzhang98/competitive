import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution(*args):
    intervals, = args
    N = len(intervals)
    for i in range(N):
        intervals[i].append(i)
    intervals.sort(key=lambda tup: tup[0])
    sequence = [""]*N
    C_end, J_end = 0, 0
    for start, end, i in intervals:
        if start >= C_end:
            C_end = end
            sequence[i] = 'C'
        elif start >= J_end:
            J_end = end
            sequence[i] = 'J'
        else:
            return "IMPOSSIBLE"
    return "".join(sequence)

T = int(input()) # read num test cases
for case_num in range(1, T + 1):

    N = int(input())
    intervals = []
    for i in range(N):
        intervals.append(list(map(int, input().split(" "))))

    res = solution(intervals)
    print("Case #{}: {}".format(case_num, res))
