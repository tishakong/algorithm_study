#include <iostream>
using namespace std;
#include <vector>
#include <algorithm>

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    vector<int> lst(n);
    
    for (int i = 0 ; i < n ; i++){
        cin >> lst[i];
    }
    
    sort(lst.begin(),lst.end());
    
    for (int i = 0 ; i < n ; i++){
        cout << lst[i] << '\n';
    }
}