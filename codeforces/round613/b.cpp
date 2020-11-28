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

ll max_subarray(vector<int>& arr) {
    ll best = 0, curr = 0;
    for (int x : arr) {
        curr += x;
        curr = max(curr, (ll) 0);
        best = max(best, curr);
    }
    return best;
}

bool solve(vector<int>& arr) {
    ll total = accumulate(begin(arr), end(arr), 0, [](ll a, ll b) {return a+b;});
    vector<int> lslice(begin(arr), end(arr)-1);
    ll left = max_subarray(lslice);
    vector<int> rslice(begin(arr)+1, end(arr));
    ll right = max_subarray(rslice);
    return total > max(left, right);
}

int main() {
    int t;
    cin >> t;
    for (int testcase = 1; testcase <= t; testcase++) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int& x : arr) {
            cin >> x;
        }
        cout << (solve(arr) ? "YES" : "NO") << endl;
    }
}
