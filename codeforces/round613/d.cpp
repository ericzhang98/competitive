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

int solve(vector<int> & arr, int b) {
    if (b == -1) return 0;
    int B = 1 << b; 
    vector<int> arr0, arr1;
    for (int x : arr) {
        if ((x & B) == B) {
            arr1.push_back(x);
        }
        else {
            arr0.push_back(x);
        }
    }

    if (arr0.size() > 0 and arr1.size() > 0) {
        return B + min(solve(arr0, b-1), solve(arr1, b-1));
    }
    else if (arr0.size() > 0) {
        return solve(arr0, b-1);
    }
    else {
        return solve(arr1, b-1);
    }
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int& x : arr) {
        cin >> x;
    }
    cout << solve(arr, 30) << endl;
}
