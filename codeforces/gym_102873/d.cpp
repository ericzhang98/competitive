#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

string solve(ll a, ll s) {
  ll b = s - a;
  if (b <= 0) return "NO";
  string x = to_string(a);
  string y = to_string(b);
  if (y.size() != x.size()) return "NO";
  map<char, int> cnts;
  for (auto c : x) cnts[c] += 1;
  map<char, int> cnts2;
  for (auto c : y) cnts2[c] += 1;
  for (auto p : cnts) {
    if (cnts2[p.first] != p.second) {
      return "NO";
    }
  }
  /*
  sort(x.begin(), x.end());
  sort(y.begin(), y.end());
  if (x != y) return "NO";
  */
  return "YES";
}

int main() {
    ll a,s;
    cin >> a >> s;
    cout << solve(a,s) << endl;
}
