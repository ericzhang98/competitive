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

ll gcd(ll a, ll b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main() {
    ll X;
    cin >> X;
    ll best = 1e12;
    for (ll i = 1; i <= sqrt(X); i++) {
        if (X % i == 0) {
            ll x = X / i;
            if (gcd(i, x) == 1) {
                best = min(best, x);
            }
        }
    }
    ll y = X / best;
    printf("%lld %lld\n", y, best);
}
