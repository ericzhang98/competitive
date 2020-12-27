#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

ll solve(string a, string b) {
  ll cnt = 0;
  int left = -1;
  for (int i = 0; i < a.size(); i++) {
    if (i >= 1) {
      string ss = a.substr(i-1, 2);
      if (ss == b) left = i-1;
    }
    cnt += (left+1);
  }
  return cnt;
}

int main() {
    int n;
    string a, b;
    cin >> n >> a >> b;
    cout << solve(a, b) << endl;
}
