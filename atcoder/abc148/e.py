N = int(raw_input())

def solve(N):
    if N % 2 == 1:
        return 0
    else:
        ans = 0
        # every n/(2 * 5^1) -> +1
        # every n/(2 * 5^2) -> +1
        # every n/(2 * 5^3) -> +1
        exp = 1
        while 2 * 5**exp <= N:
            num_div = N / (2 * 5**exp)
            ans += num_div
            exp += 1
        return ans

print solve(N)
