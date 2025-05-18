#include <iostream>
#include <queue>  // priority_queue 포함
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    //greater<int>를 사용해야 최소힙
    priority_queue<int, vector<int>, greater<int>> minHeap;

    for (int i = 0; i < N; i++) {
        int x;
        cin >> x;

        if (x == 0) {
            if (minHeap.empty()) {
                cout << 0 << '\n';
            } else {
                cout << minHeap.top() << '\n';
                minHeap.pop();
            }
        } else {
            minHeap.push(x);
        }
    }

    return 0;
}
