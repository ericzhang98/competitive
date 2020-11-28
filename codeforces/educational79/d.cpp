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
typedef pair<ll, ll> pll;

const ll MOD = 998244353;

// x, exp -> x^e mod MOD
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

ll mod_inv_prime(ll x) {
    return mod_exp(x, MOD-2);
}

ll gcd(ll a, ll b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

ll lcm(ll a, ll b) {
    return a*b/gcd(a,b);
}

// a_1/a_2 + b_1/b_2 = (a_1*b_2 + a_2*b_1)/(a_2*b_2)
// reducing only necessary if borderline out of bounds
pll frac_add(pll a, pll b) {
    if (a.first == 0) return b;
    if (b.first == 0) return a;
    ll numerator = a.first * b.second + a.second * b.first;
    ll denominator = a.second * b.second;
    ll factor = gcd(numerator, denominator);
    return {numerator / factor, denominator / factor};
}

// when doing fractions with mod at end, def don't need to reduce
ll frac_add_mod(ll a, ll b) {
    return (a + b) % MOD;
}

int main() {
    ll n;
    cin >> n;
    vector<vector<ll>> lists(n);
    for (vector<ll>& l : lists){
        ll k_i;
        cin >> k_i;
        l.resize(k_i);
        for (ll& x : l) {
            cin >> x;
        }
    }

    map<ll, ll> probs;
    map<ll, ll> gift_to_kid;
    map<ll, vector<ll>> y_containing_x;
    unordered_set<ll> all_x;
    // for (vector<int>& l : lists) {
    for (ll i = 0; i < lists.size(); i++) {
        auto l = lists[i];
        ll k_i = l.size();
        // unordered_set<ll> s;
        for (ll& x : l) {
            probs[x] = frac_add_mod(probs[x], mod_inv_prime(k_i * n));
            gift_to_kid[x]++;
            // if (s.find(x) != s.end()) { cout << "REPEAT " << i << " " << x << endl; }
            // s.insert(x);
            //y_containing_x[x].push_back(i);
            //all_x.insert(x);
        }
    }

    ll ans = 0;

    for (auto& kv : probs) {
        ll x = kv.first;
        ll prob = kv.second;
        ll kidprob = (gift_to_kid[x] * mod_inv_prime(n)) % MOD;
        ans = (ans + ((prob * kidprob) % MOD)) % MOD;
    }
    cout << ans << endl;

    /*
    ll count1 = 0;
    ans = 0;
    for (auto& x : all_x) {
        for (ll& i : y_containing_x[x]) {
            ll k_i = lists[i].size();
            // cout << i << " contains " << x << " with size " << lists[i].size() << endl;
            ans = (ans + (gift_to_kid[x] * mod_inv_prime(k_i * n * n))) % MOD;
            if (ans < 0) {cout << "wtf " << ans << " " << gift_to_kid[x] << " " << n << " " << k_i << " " << n * n * k_i << " " << mod_inv_prime(n * n * k_i) << endl;}
            count1++;
        }
    }
    // cout << ans << endl;
    */

    /*
    ll count2 = 0;
    //ans = 0;
    for (int i = 0; i < n; i++) {
        ll k_i = lists[i].size();
        for (int& x : lists[i]) {
            // ans = (ans + gift_to_kid[x] * mod_inv_prime(k_i * n * n)) % MOD;
            count2++;
        }
    }
    if (count1 != count2) {cout << "wtf " << count1 << " " << count2 << endl;}
    */
    // cout << ans << endl;


    /*
    vector<ll> cprobs;
    for (vector<int>& l : lists) { 
        ll cprob = 0;
        for (int& x : l) {
            cprob = frac_add_mod(cprob, probs[x]);
        }
        cprobs.push_back(cprob);
    }

    // normalize and sum
    ll ans = accumulate(begin(cprobs), end(cprobs), 0, [](ll a, ll b) {
            return frac_add_mod(a, b);
    });

    ans = (mod_inv_prime(n) * ans) % MOD;

    cout << ans << endl;
    */
}
