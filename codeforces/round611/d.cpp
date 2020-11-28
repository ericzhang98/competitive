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

void solve() {

}

int main() {
    int n, m; cin >> n >> m;
    vector<int> trees(n);
    for (int& x : trees) cin >> x;

    set<int> occupied(begin(trees), end(trees));
    ll total = 0;
    vector<int> res;

    deque<tuple<int,int>> q;
    for (int x : trees) {
        q.push_back(make_tuple(0, x));
    }

    while (occupied.size() < n+m) {
        int dist, curr;
        tie(dist, curr) = q.front();
        q.pop_front();
        if (!occupied.count(curr)) {
            occupied.insert(curr);
            res.push_back(curr);
            total += dist;
        }
        vector<int> neigh = {curr-1, curr+1};
        for (int ne : neigh) {
            if (!occupied.count(ne)) {
                q.push_back(make_tuple(dist+1, ne));
            }
        }
    }

    cout << total << endl;
    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << " \n"[i == res.size()-1];
    }

}
