#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

string solve(int a, vector<int>& nums) {
  set<int> s;
  for (int i = 1; i <= a; i++) s.insert(i);
  for (auto x : nums) s.extract(x);
  if (s.size() == 1) return "YES";
  return "NO";
}

int main() {
  int a,b;
  cin >> a >> b;
  vector<int> nums(b);
  for (auto& x : nums) cin >> x;
  cout << solve(a, nums) << endl;
}
