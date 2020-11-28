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

pair<int, int> solve(vector<int>& arr) {
    /*
    int ma = 0, mi = 1e9;
    for (int x : arr) {
        ma = max(ma, x);
        mi = min(mi, x);
    }
    if (ma - mi >= arr.size()) {
        return {1, arr.size()};
    }
    */

    for (int i = 1; i < arr.size(); i++) {
        if (abs(arr[i] - arr[i-1]) > 1) {
            return {i, i+1};
        }
    }

    return {-1, -1};
}

int main() {
    int t;
    cin >> t;
    for (int testcase = 1; testcase <= t; testcase++) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (auto& x : arr) cin >> x;
        auto res = solve(arr);
        if (res.first == -1) {
            cout << "NO" << endl;
        }
        else {
            printf("YES\n%d %d\n", res.first, res.second);
        }
    }
}
