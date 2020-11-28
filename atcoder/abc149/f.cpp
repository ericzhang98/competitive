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

const ll MOD = 1e9 + 7;

int N;
unordered_set<int> visited;
map<int, vector<int>> edges;
map<int, vector<int>> subtree_sizes;

ll mod_exp(ll x, ll exp) {
    ll ans = 1;
    ll base = x % MOD;
    while (exp > 0) {
        if (exp % 2 == 1) {
            ans = (ans * base) % MOD;
        }
        base = (base * base) % MOD;
        exp /= 2;
    }
    return ans;
}

ll mod_inv_prime(ll x) {
    return mod_exp(x, MOD-2);
}

int dfs(int v) {
    // cout << v << endl;
    visited.insert(v);
    int total_size = 0;
    for (int ne : edges[v]) {
        // cout << "attempt visit " << ne << endl;
        if (!visited.count(ne)) { 
            int subtree_size = dfs(ne) + 1;
            // cout << "subtree size " << subtree_size << endl;
            if (subtree_size > 0) {
                subtree_sizes[v].push_back(subtree_size);
            }
            total_size += subtree_size;
        }
    }
    if (N - 1 - total_size > 0) {
        subtree_sizes[v].push_back(N-1-total_size);
    }
    return total_size;
}

int main() {
    cin >> N;
    for (int i = 0; i < N-1; i++) {
        int a, b;
        cin >> a >> b;
        edges[a-1].push_back(b-1);
        edges[b-1].push_back(a-1);
    }

    dfs(0);

    ll two_inv = mod_inv_prime(2);
    vector<ll> two_inv_pow = {1};
    ll curr = 1;
    for (int i = 0; i < N; i++) {
        curr = (curr * two_inv) % MOD;
        two_inv_pow.push_back(curr);
    }

    ll ev = 0;
    for (int i = 0; i < N; i++) {
        if (subtree_sizes[i].size() < 2) continue;
        ll p_all_white = 1;
        for (int subtree_size : subtree_sizes[i]) {
            p_all_white = (p_all_white * two_inv_pow[subtree_size]) % MOD;
        }
        ll p_one_black = 0;
        for (int subtree_size : subtree_sizes[i]) {
            ll p_t_white = two_inv_pow[subtree_size];
            ll p_t_black = (1 - p_t_white + MOD) % MOD;
            ll prob = (p_all_white * ((p_t_black * mod_inv_prime(p_t_white)) % MOD)) % MOD;
            p_one_black = (p_one_black + prob) % MOD;
        }
        ll cond_prob = (1 - ((p_all_white + p_one_black) % MOD) + MOD) % MOD;
        ll total_prob = (two_inv * cond_prob) % MOD;
        ev = (ev + total_prob) % MOD;
    }

    cout << ev << endl;
}
