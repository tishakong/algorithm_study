#include <iostream>
#include <map>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, m; //갖고있는 카드 개수, 구해야할 카드
    map<int, int> card;
    int tmp;
    cin >> n;
  
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        card[tmp]++;
    }

    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> tmp;
        cout << card[tmp] << " ";
    }

    return 0;
}