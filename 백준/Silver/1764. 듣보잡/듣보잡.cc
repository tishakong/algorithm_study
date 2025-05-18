#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M; //첫 조건 수, 두번째 조건 수
    cin >> N >> M;

    set<string> first;
    vector<string> result;

    //첫 조건 대상자 리스트 셋
    for (int i = 0; i < N; i++) {
        string name;
        cin >> name;
        first.insert(name);
    }

    //두 번째 대상자 존재하는지 확인
    for (int i = 0; i < M; i++) {
        string name;
        cin >> name;
        if (first.count(name)) {
            result.push_back(name);
        }
    }

    sort(result.begin(), result.end());

    cout << result.size() << '\n';
    for (string& name : result) {
        cout << name << '\n';
    }

    return 0;
}
