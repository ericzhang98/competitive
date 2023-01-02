# t = int(input())

N = 10**6
MOD = 10**9 + 7
FACT = [1]*(N+1)
for x in range(1, N+1):
    FACT[x] = (FACT[x-1]*x) % MOD
INVFACT = [1]*(N+1)
INVFACT[N] = pow(FACT[N], MOD-2, MOD)
for x in range(N-1, 0, -1):
    INVFACT[x] = (INVFACT[x+1]*(x+1)) % MOD
THREE_POW = [1]*(N+1)
for x in range(1, N+1):
    THREE_POW[x] = (THREE_POW[x-1] * 3) % MOD

def nCk(n, k):
    if n < k:
        return 0
    return (FACT[n] * INVFACT[k] * INVFACT[n-k]) % MOD

def soln(n, k):
    # for n there are 2^n * 2^n bitsum combos
    # 1 -- 4
    # (1,0) -- 3; (1,1) -- 1
    # (1,0) -- 1 with no front carry, 2 with front carry; (1,1) -- 1 with full carry
    # 2 -- 16
    # (2,0) --  9; (2,1) -- 6; (2,2) -- 1
    # 3 -- 64
    # (3,0) -- 27; (3,1) -- 27; (3,2) -- ; (3,3) -- 1
    # (n,n) always 1
    # (2,2) = (1,1) * (1,1)
    # (2,1) = (1,0) * (1,1) + (1,1) * (1,0)
    # (2,0) = (1,0) * (1,0)
    # (3,0) = (1,0) * (2,0)
    # (3,1) = (1,0) * (2,1) + (1,1) * (2,0)
    # (3,2) = (1,0) * (2,2) + (1,1) * (2,1)
    # (n,k) = (1,0) * (n-1,k) + (1,1) * (n-1,k-1) = 3 * (n-1,k) + (n-1,k-1)
    # nvm, doesn't work
    # carry in + carry out = 3
    # no carry in + no carry out = 3
    # carry in + no carry out = 1
    # no carry in + carry out = 1
    # for a given k, break the problem down into q "switches" (a switch between carry in and carry out)
    # there are q=0..n switches, and 3^(n-q) * (k-1 choose ceil(q/2)-1) * ((n-k+1)-1 choose floor(q/2)) choices given q
    # cuz we have k-1 carries and n-k+1 non-carries
    if k == 0:
        return THREE_POW[n]
    ans = 0
    for q in range(1, min(n,2*k)+1):
        combos = (THREE_POW[n-q] * nCk(k-1, (q+1)//2-1) * nCk(n-k+1-1, q//2)) % MOD
        ans = (ans + combos) % MOD
    return ans

# for _ in range(t):
n, k = map(int, input().split())
ans = soln(n, k)
print(ans)
