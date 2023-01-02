#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

string solve(vector<int> p1, vector<int> p2, vector<int> p3) {
  if ((p1[0] == p2[0] || p2[0] == p3[0] || p3[0] == p1[0]) &&
   (p1[1] == p2[1] || p2[1] == p3[1] || p3[1] == p1[1])) {
      return "NO";
    }
  return "YES";
}

int main() {
    int t; cin >> t;
    for (int testcase = 1; testcase <= t; testcase++) {
      vector<int> p1(2), p2(2), p3(3);
      cin >> p1[0] >> p1[1];
      cin >> p2[0] >> p2[1];
      cin >> p3[0] >> p3[1];
      cout << solve(p1, p2, p3) << endl;
    }
}
