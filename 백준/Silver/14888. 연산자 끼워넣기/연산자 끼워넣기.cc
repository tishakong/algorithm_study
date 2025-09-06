#include <bits/stdc++.h>
using namespace std;

int N;
int arr[11], op[4];
long long maxResult, minResult;

void dfs(int idx, long long current) {
    if (idx == N) {
        if (current > maxResult) maxResult = current;
        if (current < minResult) minResult = current;
        return;
    }
    if (op[0] > 0) {
        op[0]--;
        dfs(idx+1, current + arr[idx]);
        op[0]++;
    }
    if (op[1] > 0) {
        op[1]--;
        dfs(idx+1, current - arr[idx]);
        op[1]++;
    }
    if (op[2] > 0) {
        op[2]--;
        dfs(idx+1, current * arr[idx]);
        op[2]++;
    }
    if (op[3] > 0) {
        op[3]--;
        long long next;
        // 명시적 음수 처리 (C++ 표준과 일치: trunc toward zero)
        if (current < 0) next = - ( ( -current ) / arr[idx] );
        else next = current / arr[idx];
        dfs(idx+1, next);
        op[3]++;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    for (int i = 0; i < N; ++i) cin >> arr[i];
    for (int i = 0; i < 4; ++i) cin >> op[i];

    maxResult = LLONG_MIN;
    minResult = LLONG_MAX;
    dfs(1, arr[0]);
    cout << maxResult << '\n' << minResult << '\n';
    return 0;
}
