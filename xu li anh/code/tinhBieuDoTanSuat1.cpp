#include<iostream>
#include<map>
using namespace std;

int main() {
    int m, n;
    cin >> m >> n;
    int a[m][n];
    map<int, int> mp;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
            mp[a[i][j]]++;
        }
    }
    for(auto i: mp) {
        cout << i.first << " " << i.second << endl;
    }
}
