#include <iostream>
#include <climits>
using namespace std;

int N;
int arr[11], op[4];          // arr: 숫자 배열, op: +, -, *, / 개수
int maxResult = INT_MIN;
int minResult = INT_MAX;

void dfs(int idx, int current) {
    if (idx == N) {
        // 모든 수를 다 사용했을 때 결과 갱신
        maxResult = max(maxResult, current);
        minResult = min(minResult, current);
        return;
    }
    // 덧셈
    if (op[0] > 0) {
        op[0]--;
        dfs(idx+1, current + arr[idx]);
        op[0]++;
    }
    // 뺄셈
    if (op[1] > 0) {
        op[1]--;
        dfs(idx+1, current - arr[idx]);
        op[1]++;
    }
    // 곱셈
    if (op[2] > 0) {
        op[2]--;
        dfs(idx+1, current * arr[idx]);
        op[2]++;
    }
    // 나눗셈 (C++14 기준: 음수도 절댓값으로 나눈 몫을 취하고, 결과에 부호를 붙인다)
    if (op[3] > 0) {
        op[3]--;
        dfs(idx+1, current / arr[idx]);
        op[3]++;
    }
}

int main() {
    cin >> N;
    for(int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    for(int i = 0; i < 4; i++) {
        cin >> op[i];
    }
    // 첫 번째 숫자를 시작값으로 하여 dfs 호출
    dfs(1, arr[0]);
    cout << maxResult << "\n" << minResult << endl;
    return 0;
}
