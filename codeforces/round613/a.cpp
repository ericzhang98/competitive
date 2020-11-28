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

void solve() {

}

int main() {
    int x;
    cin >> x;
    int lcnt = 0, rcnt = 0;
    for (int i = 0; i < x; i++) {
        char a;
        cin >> a;
        if (a == 'L') lcnt += 1;
        if (a == 'R') rcnt += 1;
    }
    int ans = lcnt + rcnt + 1;
    cout << ans << endl;
}
