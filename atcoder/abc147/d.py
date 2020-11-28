import numpy as np

N = int(raw_input())
A = np.array(map(int, raw_input().split()))
# A = map(lambda x: format(x, '060b'), A)
MOD = 10**9 + 7

count = dict()
for i in range(60):
    # zeros = len([a[i] for a in A if a[i] == '0'])
    zeros = np.count_nonzero((A>>i)&1)
    ones = N - zeros
    count[i] = zeros*ones

ans = 0
for i in count:
    ans = (ans + count[i] * pow(2,i,MOD)) % MOD

print ans
