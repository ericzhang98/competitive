def solve(hh, mm):
    dh = 23 - hh
    dm = 60 - mm
    ans = dh*60 + dm
    print ans

t = int(raw_input())

for _ in range(t):
    hh, mm = map(int, raw_input().split())
    solve(hh, mm)
