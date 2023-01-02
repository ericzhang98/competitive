#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

vector<int> solve(vector<int> b) {
  int n = b.size();
  vector<int> counts(2, 0);
  for (auto x : b) {
    counts[x] += 1;
  }
  int bot = pow(2, counts[1]);
  int top = pow(2, n) - (pow(2, counts[0]) - 1);
  vector<int> ans;
  for (int x = bot; x <= top; x++) {
    ans.push_back(x);
  }
  return ans;
}

int main() {
    int n; cin >> n;
    string s; cin >> s;
    vector<int> b;
    for(int i = 0; i < s.size(); i++) {
      b.push_back(s[i] - '0');
    }
    auto ans = solve(b);
    for (int i = 0; i < ans.size(); i++) {
      cout << ans[i] << " \n"[i==ans.size()-1];
    }
}
