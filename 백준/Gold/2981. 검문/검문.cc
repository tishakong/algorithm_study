#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int gcd(int a, int b) {
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;

    vector<int> nums(N);
    for (int i = 0; i < N; ++i) {
        cin >> nums[i];
    }

    sort(nums.begin(), nums.end());

    int curGCD = nums[1] - nums[0];
    for (int i = 2; i < N; ++i) {
        curGCD = gcd(curGCD, nums[i] - nums[i - 1]);
    }

    vector<int> result;
    for (int i = 2; i <= sqrt(curGCD); ++i) {
        if (curGCD % i == 0) {
            result.push_back(i);
            if (i != curGCD / i)
                result.push_back(curGCD / i);
        }
    }
    result.push_back(curGCD);

    sort(result.begin(), result.end());

    for (int m : result) {
        cout << m << " ";
    }

    return 0;
}
