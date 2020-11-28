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

ll count(vector<ll>& A, ll amount) {
    ll N = A.size();
    ll cnt = 0;
    for (ll i = 0; i < N; i++) {
        ll left = A[i];
        ll right = amount - left;
        // bsearch smallest index s.t. A[j] >= right
        ll lo = 0, hi = N-1;
        while (lo < hi) {
            ll mid = (lo + hi) / 2;
            if (A[mid] >= right) hi = mid;
            else lo = mid+1;
        }
        ll lo2 = lower_bound(begin(A), end(A), right) - begin(A);
        if (A[i] + A[lo] < amount) lo = N;
        cnt += (N - lo2);
    }
    return cnt;
}

int main() {
    ll N, M;
    cin >> N >> M;
    vector<ll> A(N);
    for (auto& a : A) {
        cin >> a;
    }
    sort(begin(A), end(A));
    ll lo = 0, hi = A.back() * 2;

    // bsearch largest amount s.t. count(A, amount) >= M
    while (lo < hi) {
        ll mid = (lo + hi + 1) / 2;
        // printf("%lld %lld\n", mid, count(A, mid));
        if (count(A, mid) >= M) {
            lo = mid;
        }
        else {
            hi = mid - 1;
        }
    }

    // cout << lo << endl;

    vector<ll> pfs = {0};
    for (auto& x : A) {
        pfs.push_back(pfs.back() + x);
    }

    ll ans = 0;
    for (ll i = 0; i < N; i++) {
        ll left = A[i];
        ll right = lo - left;
        ll j = lower_bound(begin(A), end(A), right) - begin(A);
        ans += (left * (N - j));
        ans += (pfs[N] - pfs[j]);
    }
    ans -= (count(A, lo) - M) * lo;

    cout << ans << endl;
}
