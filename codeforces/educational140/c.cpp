#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
ll MOD = 998244353;

ll solve(vector<vector<ll>> constraints) {
  // non-0 solution must have: no 2's before 1's
  // store map of indices to 1-segment leftmost bound
  // store map of indices to 2-segment rightmost bound
  ll n = constraints.size();
  int INF = n;
  vector<int> left_1segment(n, INF);
  vector<int> left_2segment(n, -INF);
  for (int i = 0; i < n; i++) {
    auto constraint = constraints[i];
    if (constraint[0] == 2) {
      return 0;
    }
    for (int j = i+1; j < n; j++) {
      auto a = constraint[j-i];
      if (a == 1) {
        left_1segment[j] = min(left_1segment[j], i);
      }
      else if (a == 2) {
        left_2segment[j] = max(left_2segment[j], i);
      }
    }
  }
  // dp on valid solution count for (valid string until index i, right most switch happened between j-1 and j)
  // each index is either part of: nothing / different segment, same 1-segment, same 2-segment, both same 1-segment and same 2-segment
  // if nothing, the new bit can either stay the same or switch:
  // - copy over all switch counts from dp[i-1][j] to dp[i][j], j<i
  // - sum up all dp[i-1][j] switch counts for dp[i][i], j<i
  // if 1-segment, the new bit must stay the same and no switch can happen after left bound:
  // - copy over all switch counts from dp[i-1][j] to dp[i][j], j<=left_1segment
  // if 2-segment, the new bit can stay the same if switch occurred within left bound, or switch:
  // - copy over all switch counts from dp[i-1][j] to dp[i][j], left_2segment<j<i
  // - sum up all dp[i-1][j] switch counts for dp[i][i], j<i
  // if 1-segment and 2-segment, the new bit must stay the same and no switch can happen after 1-segment left bound and we drop switches before 2-segment left bound:
  // - copy over all switch counts from dp[i-1][j] to d[i][j], left_2segment<j<=left_1segment
  // final answer is 2 * sum of all valid strings until index n-1 across all switch indices
  // starting case is [1]
  // can do 1-d dp cuz we only use dp[i-1]
  vector<ll> dp(n, 0);
  dp[0] = 1;
  for (int i = 1; i < n; i++) {
    // cerr << "bruh" << i << endl;
    vector<ll> nxt(n, 0);
    if (left_1segment[i] == INF && left_2segment[i] == -INF) {
      // cerr << "nothing" << endl;
      ll total = accumulate(dp.begin(), dp.begin() + i, (ll) 0);
      for (int j = 0; j < i; j++) {
        nxt[j] = dp[j];
      }
      nxt[i] = total % MOD;
    }
    else if (left_1segment[i] != INF && left_2segment[i] == -INF) {
      // cerr << "1 segment only" << endl;
      for (int j = 0; j <= left_1segment[i]; j++) {
        nxt[j] = dp[j];
      }
    }
    else if (left_1segment[i] == INF && left_2segment[i] != -INF) {
      // cerr << "2 segment only" << endl;
      ll total = accumulate(dp.begin(), dp.begin() + i, (ll) 0);
      for (int j = left_2segment[i] + 1; j < i; j++) {
        nxt[j] = dp[j];
      }
      nxt[i] = total % MOD;
    }
    else {
      // cerr << "both" << endl;
      for (int j = left_2segment[i] + 1; j <= left_1segment[i]; j++) {
        nxt[j] = dp[j];
      }
    }
    dp = nxt;
  }
  // cerr << "done" << endl;
  auto total = accumulate(dp.begin(), dp.end(), (ll) 0);
  return (2 * total) % MOD;
}

int main() {
    int n; cin >> n;
    vector<vector<ll>> constraints;
    for (int i = 0; i < n; i++) {
      vector<ll> constraint(n - i);
      for (auto& x: constraint) cin >> x;
      constraints.push_back(constraint);
    }
    cout << solve(constraints) << endl;
}
