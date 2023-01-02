#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

ll solve(vector<ll> arr) {
  ll first = arr[0];
  vector<ll> rest = vector<ll>(arr.begin() + 1, arr.end());
  sort(rest.begin(), rest.end());
  for (auto x : rest) {
    if(x > first) {
      ll amt = (x - first + 1) / 2;
      first += amt;
    }
  }
  return first;
}

int main() {
    int t; cin >> t;
    for (int testcase = 1; testcase <= t; testcase++) {
        int n; cin >> n;
        vector<ll> arr(n);
        for (auto& x : arr) cin >> x;
        cout << solve(arr) << endl;
    }
}
