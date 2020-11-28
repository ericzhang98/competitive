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
#include <set>
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
using ll = long long;

int soln(int n, int s, vector<ll>& a) {
    ll total = 0, m = 0;
    int i = 0, mi = 0;
    for (; i < n; i++) {
        total += a[i];
        m = max(m, a[i]);
        if (total - m > s) {
            break;
        }
    }
    if (total <= s) {return 0;}
    m = 0;
    for (int j = 0; j < i; j++) {
        if (a[j] > m) {
            m = a[j];
            mi = j;
        }
    }
    return mi + 1;
    /*
    int acc = accumulate(a, a+n, 0, [](int a, int b) {return a+b;});
    if (acc <= s) {
        return 0;
    }
    int m = -1, mi = 0, total = 0;
    for (int i = 0; i < n; i++) {
        bool upd = false;
        total += a[i];
        if (a[i] > m) {
            m = a[i];
            upd = true;
        }
        // cout << total - m << endl;
        if (total - m > s) {
            return mi;
        }
        if (upd) {
            mi = i+1;
            //cout << "update " << mi << endl;
        }
    }
    return mi;
    */
    /*
    priority_queue<pair<int, int>> pq;
    int ptr1 = 0, ptr2 = 0;
    int best = 0, besti = 0, total = 0;
    while (ptr2 < n) {
        total += a[ptr2];
        pq.push({a[ptr2], ptr2});
        while (total - pq.top().first > s) {
            total -= a[ptr1];
            ptr1++;
            while (pq.top().second < ptr1) {
                pq.pop();
            }
        }
        if (ptr2 - ptr1 + 1 > best) {
            best = ptr2 - ptr1 + 1;
            besti = pq.top().second + 1;
        }
        ptr2++;
    }
    return besti;
    */
}


int main() {
    // get a integer
    int t;
    cin >> t;
    // get two integers separated with half-width break
    for (int i = 1; i <= t; i++) {
        int n, s;
        cin >> n >> s;
        vector<ll> v(n);
        for (auto& x : v) {
            cin >> x;
        }
        cout << soln(n, s, v) << endl;
    }
}
