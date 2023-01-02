#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const int N = 1e7;
vector<int> PRIMES;
vector<bool> isPrime(N+1, true);
vector<int> primeDivisor(N+1);
// bool isPrime[N+1];
// int primeDivisor[N+1];

int solve(int x, int y) {
  // (x+k, y+k) becomes coprime when (x+k, y-x) becomes coprime
  // consider all prime factors of y-x and choose min k s.t. (x+k, y-x) is coprime
  // min k s.t. d | x+k is -x % d == ((-x % d) + d) % d in cpp
  if (x > y) swap(x,y);
  int diff = y - x;
  if (diff == 1) {
    return -1;
  }
  int ans = N;
  while(diff > 1) {
    int divisor = primeDivisor[diff];
    int cand = ((-x % divisor) + divisor) % divisor;
    ans = min(ans, cand);
    diff = diff / divisor;
  }
  if (ans == N) {
    return -1;
  }
  return ans;
}

int main() {
  for (int x = 0; x <= N; x++) {
    isPrime[x] = true;
    primeDivisor[x] = x;
  }
  // sieve
  for (int divisor = 2; divisor*divisor <= N; divisor++) {
    if (isPrime[divisor]) {
      for (int x = divisor*divisor; x <= N; x += divisor) {
        isPrime[x] = false;
        primeDivisor[x] = min(divisor, primeDivisor[x]);
      }
    }
  }
  // for (int divisor = 2; divisor <= N; divisor++) {
  //   if (isPrime[divisor]) {
  //     PRIMES.push_back(divisor);
  //   }
  // }
  ios_base::sync_with_stdio(false);
	cin.tie(0), cout.tie(0);
  int t; cin >> t;
  for (int testcase = 1; testcase <= t; testcase++) {
      int x, y; cin >> x >> y;
      cout << solve(x, y) << endl;
  }
}
