#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

string solve(string a, string b) {
  int n = a.size();
  vector<bool> dp = {true, true};
  for (int i = 0; i < n; i++) {
    if (a[i] == 'B' && b[i] == 'B') {
      swap(dp[0], dp[1]);
    }
    else if (a[i] == 'B') {
      if (dp[0]) {
        dp[1] = false;
      }
      else {
        return "NO";
      }
    }
    else if (b[i] == 'B') {
      if (dp[1]) {
        dp[0] = false;
      }
      else {
        return "NO";
      }
    }
    else {
      return "NO";
    }
  }
  return "YES";
}

int main() {
    int t; cin >> t;
    for (int testcase = 1; testcase <= t; testcase++) {
        int n; cin >> n;
        string a, b; cin >> a >> b;
        cout << solve(a, b) << endl;
    }
}
