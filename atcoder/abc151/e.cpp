#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;
typedef long long ll;

ll MOD = 1e9 + 7;

vector<ll> factorial;
ll mod_exp(ll x, ll exp) {
    ll res = 1;
    ll base = x % MOD;
    while (exp) {
        if (exp % 2 == 1) {
            res = (res * base) % MOD;
        }
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

ll nCk(ll n, ll k) {
    if (n < k) return 0;
    ll numerator = factorial[n];
    ll denominator = (factorial[n-k] * factorial[k]) % MOD;
    ll ans = (numerator * mod_exp(denominator, MOD-2)) % MOD;
    return ans;
}

int main() {
    ll N, K; cin >> N >> K;
    vector<ll> nums(N);
    for (ll& x : nums) {
        cin >> x;
    }

    factorial = {1};
    for (ll i = 1; i <= N; i++) {
        factorial.push_back((factorial.back() * i) % MOD);
    }

    ll ans = 0;

    sort(begin(nums), end(nums), [](ll a, ll b){return a > b;});
    for (ll i = 0; i < N-K+1; i++) {
        ll best = (MOD + nums[i]) % MOD;
        ll contribution = (best * nCk(N-i-1, K-1)) % MOD;
        ans = (ans + contribution) % MOD;
    }

    sort(begin(nums), end(nums));
    for (ll i = 0; i < N-K+1; i++) {
        ll best = nums[i] % MOD;
        ll contribution = (best * nCk(N-i-1, K-1)) % MOD;
        ans = (ans + MOD - contribution) % MOD;
    }

    cout << ans << endl;
}
