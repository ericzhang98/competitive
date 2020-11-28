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

ll solve(vector<int>& a, vector<int>& b) {
    ll tot = 0, curr = 0, k = 0;
    unordered_set<int> seen;
    for (int i = 0; i < a.size(); i++) {
        if (curr == b.size()) break;
        if (a[i] == b[curr]) {
            tot += (2*k + 1);
            curr += 1;
            k -= 1;
            while (curr < b.size() and seen.find(b[curr]) != seen.end()) {
                tot += 1;
                curr += 1;
                k -= 1;
            }
        }
        seen.insert(a[i]);
        k += 1;
    }
    /*
    int i = 0;
    while (curr < b.size()) {
        if (seen.find(b[curr]) != seen.end()) {
            tot += 1;
            curr += 1;
            k -= 1;
        }
        else if (a[i] == b[curr]) {
            tot += 2*k + 1;
            curr += 1;
            k -= 1;
        }
        else {
            seen.insert(a[i]);
            k += 1;
            i += 1;
        }
    }
    */
    /*
    int i = 0;
    for (int bcurr : b) {
        if (seen.find(bcurr) != seen.end()) {
            tot += 1;
            curr += 1;
            k -= 1;
            continue;
        }
        int stk = k;
        while (i < a.size()) {
            if (a[i] == bcurr) {
                tot += 2*stk + 1;
                i += 1;
                curr += 1;
                break;
            }
            else {
                seen.insert(a[i]);
                i += 1;
                k += 1;
                stk += 1;
            }
        }
    }
    */

    return tot;
}

int main() {
    int t;
    cin >> t;
    for (int testcase = 1; testcase <= t; testcase++) {
        int n, m;
        cin >> n >> m;
        vector<int> a(n), b(m);
        for (auto& x : a) {
            cin >> x;
        }
        for (auto& x : b) {
            cin >> x;
        }
        cout << solve(a, b) << endl;
    }
}
