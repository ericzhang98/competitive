#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

string solve(int n) {
  if (n % 4 == 2) return "Alice";
  else if (n % 2 == 0) return "Draw";
  else return "Bob";
}

int main() {
    int t; cin >> t;
    for (int testcase = 1; testcase <= t; testcase++) {
        int n; cin >> n;
        cout << solve(n) << endl;
    }
}
