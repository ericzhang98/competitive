#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

ll solve(vector<ll>& nums) {
  ll curr = -1e9;
  ll i = 0;
  while(i < nums.size()) {
    if (nums[i] < curr) break;
    curr = nums[i];
    i++;
  }
  i--;
  curr = -1e9;
  ll j = nums.size()-1;
  while(j >= 0) {
    if (nums[j] < curr) break;
    curr = nums[j];
    j--;
  }
  j++;
  j = max(i+1, j);
  ll ans = (i+1) + (nums.size()-j);
  return ans;
}

int main() {
    int n; cin >> n;
    vector<ll> nums(n);
    for (auto& x : nums) cin >> x;
    cout << solve(nums) << endl;
}
