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

string soln(int a, int b, int c) {
    int x = max(a, max(b, c));
    int y = a + b + c - x;
    return x <= y+1 ? "Yes" : "No";
}

int main() {
    // get a integer
    int t, a, b, c;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> a >> b >> c;
        cout << soln(a, b, c) << endl;
    }
}
