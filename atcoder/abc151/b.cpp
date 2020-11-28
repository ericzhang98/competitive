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
    int N, K, M;
    cin >> N >> K >> M;
    int total = 0;
    for (int i = 0; i < N-1; i++) {
        int x;
        cin >> x;
        total += x;
    }
    int target = N*M - total;
    if (target <= 0) {
        cout << 0 << endl;
    }
    else if (target > K) {
        cout << -1 << endl;
    }
    else{
        cout << target << endl;
    }
}
