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
    int N, M;
    cin >> N >> M;
    set<int> accepted;
    map<int, int> wa;
    for (int i = 0; i < M; i++) {
        int p;
        string verdict;
        cin >> p >> verdict;
        if (accepted.count(p)) {
            continue;
        }

        if (verdict == "AC") {
            accepted.insert(p);
        }
        else {
            wa[p] += 1;
        }
    }
    int totalwa = 0;
    for (auto& kv : wa) {
        int k, v;
        tie(k, v) = kv;
        if (accepted.count(k)) totalwa += v;
    }
    printf("%lu %d\n", accepted.size(), totalwa);
}
