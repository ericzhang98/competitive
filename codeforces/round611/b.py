def solve(n, k):
    remain = n % k
    cant = remain - k/2
    ans = n - max(0, cant)
    print ans

t = int(raw_input())

for _ in range(t):
    n, k = map(int, raw_input().split())
    solve(n, k)
