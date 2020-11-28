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

using namespace std;
typedef long long ll;

int main() {
    int t;
    cin >> t;
    for (int testcase = 1; testcase <= t; testcase++) {
        int n;
        ll b = 0, c = 0;
        cin >> n;
        for (int i = 0; i < n; i++) {
            int a;
            cin >> a;
            b += a;
            c ^= a;
        }
        ll BIG = (ll) 1 << 50;
        vector<ll> res = {BIG + c, (BIG - b - c) >> 1, (BIG - b - c) >> 1};
        printf("3\n%lld %lld %lld\n", res[0], res[1], res[2]);
        /*
        ll su = b + res[0]+res[1]+res[2];
        ll xo = c ^ res[0]^res[1]^res[2];
        printf("%lld, %lld\n", su, xo);
        */
    }
}
