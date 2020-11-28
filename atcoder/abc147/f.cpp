/********   All Required Header Files ********/
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


bool dp[80][80][6400];
int main()
{
    int H, W;
    cin >> H >> W;
    vector<vector<int>> A(H), B(H);
    int x;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cin >> x;
            A[i].push_back(x);
        }
    }
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cin >> x;
            B[i].push_back(x);
        }
    }

    memset(dp, 0, sizeof dp);
    //for (int i = 0; i < H; i++) for (int j = 0; j < W; j++) for (int k = 0; k < 6400; k++) dp[i][j][k] = false;

    dp[0][0][abs(A[0][0] - B[0][0])] = true;

    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (i == 0 && j == 0)
                continue;
            int d = abs(A[i][j] - B[i][j]);
            if (i-1 >= 0) {
                for (int k = 0; k < 6400; k++) {
                    if (dp[i-1][j][k]) {
                        int k1 = abs(k+d);
                        int k2 = abs(k-d);
                        if (k1 < 6400)
                            dp[i][j][k1] = true;
                        if (k2 < 6400)
                            dp[i][j][k2] = true;
                    }
                }
            }
            if (j-1 >= 0) {
                for (int k = 0; k < 6400; k++) {
                    if (dp[i][j-1][k]) {
                        int k1 = abs(k+d);
                        int k2 = abs(k-d);
                        if (k1 < 6400)
                            dp[i][j][k1] = true;
                        if (k2 < 6400)
                            dp[i][j][k2] = true;
                    }
                }
            }
        }
    }

    for (int k = 0; k < 6400; k++) {
        if (dp[H-1][W-1][k] == true) {
            cout << k << endl;
            return 0;
        }
    }
    return 0;
}

