#include <iostream>
#include <vector>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    vector<int> lst(n);
    
    for (int i = 0; i < n; i++){
        cin >> lst[i]; 
    }
    
    int v;
    int result = 0;
    cin >> v; 
    
    for (int i = 0; i < n; i++){
        if (lst[i] == v){
            result++;
        }
    }
    
    cout<< result;
    
    return 0;
}
