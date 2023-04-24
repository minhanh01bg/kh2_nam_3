#include <iostream>
#include <string>
using namespace std;
 
int main () {
    int n;
    cin>>n;
    for (int i=1; i<=n; i++) {
        int r;
        string s;
        cin >> r >> s;
        for (int i=0; i<s.length(); i++) {
            for (int j=1; j<=r; j++) {
                cout<<s[i];
            }
        }
        cout<<endl;
    }
    return 0;
}