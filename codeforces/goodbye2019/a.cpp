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

string solve(vector<int>& p1, vector<int>& p2) {
    int m1 = 0, m2 = 0;
    for (int x : p1) m1 = max(m1, x);
    for (int x : p2) m2 = max(m2, x);
    return m1 > m2 ? "YES" : "NO";
}

int main() {
    int t;
    cin >> t;
    for (int testcase = 1; testcase <= t; testcase++) {
        int n, k1, k2;
        cin >> n >> k1 >> k2;
        vector<int> p1(k1);
        vector<int> p2(k2);
        for (auto& x : p1) cin >> x;
        for (auto& x : p2) cin >> x;
        cout << solve(p1, p2) << endl;
    }
}
