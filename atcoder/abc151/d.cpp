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

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

vector<vector<char>> mat;
int H, W;

int maxbfs(int i, int j) {
    int res = 0;

    deque<tuple<int, int, int>> q = {make_tuple(0, i, j)};
    set<pair<int,int>> seen;

    while (q.size() > 0) {
        int dist, i, j;
        tie(dist, i, j) = q.front(); q.pop_front();
        //printf("%d %d %d\n", dist, i, j);
        pair<int, int> v = {i, j};
        if (seen.count(v)) continue;
        seen.insert(v);
        res = max(res, dist);
        for (int a = 0; a < 4; a++) {
            int i2 = i+dx[a], j2 = j+dy[a];
            if (0 <= i2 and i2 < H and 0 <= j2 and j2 < W) {
                //printf("%d %d\n", i2, j2);
                // cout << mat[i2][j2] << endl;
                if (mat[i2][j2] == '.') {
                    q.push_back(make_tuple(dist+1, i2, j2));
                }
            }
        }
    }


    /*
    for (auto& row : mat) {
        for (auto& val : row) {
            cout << val;
        }
    }
    */

    return res;
}

int main() {
    cin >> H >> W;
    mat = vector<vector<char>>(H, vector<char>(W, ' '));
    for (auto& row : mat) {
        for (auto& val : row) {
            cin >> val;
        }
    }
    int best = 0;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (mat[i][j] == '.') {
                int b = maxbfs(i,j);
                //printf("best %d\n", b);
                best = max(best, b);
            }
        }
    }
    cout << best << endl;
}
