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

unordered_map<int, int> bfs_dist(int v, unordered_map<int, vector<int>> &edges) {
    unordered_map<int, int> distances;
    unordered_set<int> seen;
    deque<tuple<int, int>> q;
    q.push_back(make_tuple(v,0));
    while (!q.empty()) {
        int curr, dist;
        tie(curr, dist) = q.front(); q.pop_front();
        if (seen.find(curr) != seen.end()) continue;
        seen.insert(curr);
        distances[curr] = dist;
        for (int ne : edges[curr]) {
            q.push_back(make_tuple(ne, dist+1));
        }
    }
    return distances;
}

int main() {
    // get a integer
    int N, u, v;
    cin >> N >> u >> v;
    unordered_map<int, vector<int>> edges;
    for (int i = 1; i < N; i++) {
      int a, b;
      cin >> a >> b;
      edges[a].push_back(b);
      edges[b].push_back(a);
    }
    auto udist = bfs_dist(u, edges);
    auto vdist = bfs_dist(v, edges);
    int bestdist = -INF;
    for (int i = 1; i < N+1; i++) {
       if (udist[i] < vdist[i]) {
           bestdist = max(bestdist, vdist[i]);
       }
    }
    cout << bestdist-1 << endl;
}
