#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

ll solve(vector<int> nums) {
  sort(nums.begin(), nums.end());
  int median = nums[nums.size()/2];
  ll ans = 0;
  for (auto x : nums) {
    ans += abs(median - x);
  }
  return ans;
}

int main() {
    int n; cin >> n;
    vector<int> nums(n);
    for (auto& x : nums) cin >> x;
    cout << solve(nums) << endl;
}
