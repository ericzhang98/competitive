#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

#define MOD 1000000007
#define INF 1e9
#define sum(a) accumulate(begin(a), end(a), 0, [](int a, int b) {return a+b;})

using namespace std;
using ll = long long;

ll gcd(ll A, ll B) {
    if (B == 0) return A;
    return gcd(B, A % B);
}

auto gcd2 = [](ll A, ll B) {
    while (B != 0) {
        ll a = B; ll b = A % B;
        A = a; B = b;
    }
    return A;
};

int main() {
    ll A, B;
    cin >> A >> B;
    ll lcm = A * B / gcd2(A,B);
    cout << lcm << endl;
}

