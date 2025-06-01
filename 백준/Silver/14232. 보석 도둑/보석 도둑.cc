#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long long k;
    cin >> k;

    vector<long long> factors;

    for (long long i = 2; i * i <= k; ++i) {
        while (k % i == 0) {
            factors.push_back(i);
            k /= i;
        }
    }

    if (k > 1) {
        factors.push_back(k);
    }

    cout << factors.size() << '\n';
    for (auto f : factors) {
        cout << f << ' ';
    }
    cout << '\n';

    return 0;
}
