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

bool check_prime(int x) {
    int s = (int) floor(sqrt(x));
    for (int a = 2; a <= s; a++) {
        if (x % a == 0) return false;
    }
    return true;
}

int main() {
    int X;
    cin >> X;
    while (true) {
        if (check_prime(X)) {
            break;
        }
        X += 1;
    }
    cout << X << endl;
}
