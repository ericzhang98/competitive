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
    int N, K, R, S, P;
    string T;
    cin >> N >> K >> R >> S >> P >> T;

    int ans = 0;

    for (int start = 0; start < K; start++) {
       vector<tuple<int,int,int>> dp = {make_tuple(0,0,0)}; 
       int step = 0;
       while (start + step*K < N) {
           char c = T[start + step*K];
           auto prev = dp.back();
           int prevr, prevs, prevp, nextr, nexts, nextp;
           tie(prevr, prevs, prevp) = prev;
           nextr = max(prevs, prevp);
           nexts = max(prevr, prevp);
           nextp = max(prevr, prevs);
           if (c == 's') nextr += R;
           if (c == 'p') nexts += S;
           if (c == 'r') nextp += P;
           dp.push_back(make_tuple(nextr, nexts, nextp));
           step++;
       }
       int bestr, bests, bestp;
       tie(bestr, bests, bestp) = dp.back();
       ans += max(max(bestr, bests), bestp);
    }

    cout << ans << endl;
}
