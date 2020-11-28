H, W = map(int, raw_input().split())
A = []
B = []
for h in range(H):
    A_hj = map(int, raw_input().split())
    A.append(A_hj)
for h in range(H):
    B_hj = map(int, raw_input().split())
    B.append(B_hj)

dp = [[set() for _ in range(W)] for _ in range(H)]
dp[0][0] = {abs(A[0][0] - B[0][0])}
for i in range(H):
    for j in range(W):
        if i == 0 and j == 0: continue
        d = abs(A[i][j] - B[i][j])
        possible = set()
        if i-1 >= 0:
            for diff in dp[i-1][j]:
                possible.add(abs(diff+d))
                possible.add(abs(diff-d))
        if j-1 >= 0:
            for diff in dp[i][j-1]:
                possible.add(abs(diff+d))
                possible.add(abs(diff-d))
        dp[i][j] = {d for d in possible if d <= 6400}

possible = dp[H-1][W-1]
print min(possible, key=lambda d: abs(d))
