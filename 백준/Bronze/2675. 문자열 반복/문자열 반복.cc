#include <iostream>
using namespace std;
#include <string>

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int T;
    cin >> T;
    
    int R;
    string S;
    
    for (int i = 0; i<T ; i++){
        cin >> R >> S;
        
        for (char c : S){
            for (int j = 0; j< R; j++){
                cout << c;
            }
        }

        cout << '\n';
    }
    
    
    return 0;
}
