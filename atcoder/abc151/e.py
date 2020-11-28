MOD = 10**9 + 7

N, K = map(int, raw_input().split())
A = map(int, raw_input().split())

factorial = [1]
for i in range(1, N+1):
    factorial.append((i * factorial[-1]) % MOD)

def nCk(n, k):
    numerator = factorial[n]
    denominator = factorial[n-k] * factorial[k]
    return numerator * pow(denominator, MOD - 2, MOD)

ans = 0

A.sort()
for i in range(N-K+1):
    best = A[i]
    contribution = (best * nCk(N-i-1, K-1))
    ans = (ans - contribution) % MOD

A = A[::-1]
for i in range(N-K+1):
    best = A[i]
    contribution = (best * nCk(N-i-1, K-1))
    ans = (ans + contribution) % MOD

print ans
