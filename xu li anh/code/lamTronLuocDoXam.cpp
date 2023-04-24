#include <bits/stdc++.h>

using namespace std;

int smooth(int b, int W, map<int, int> mp) {
    double res = 0;
    for(int w = -(W - 1) / 2; w <= (W - 1) / 2; w++) {
        res += mp[b - w];
    }
    return round(res / W);
}

int main() {
    int m, n, W;
    cin >> m >> n;
    int a[m][n];
    map<int, int> mp, hsmooth;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
            mp[a[i][j]]++;
        }
    }
    cin >> W;
    for(auto i : mp) {
        cout << i.first << "\t";
        int b = i.first;
        hsmooth[b] = smooth(b, W, mp);
    }
    cout << endl;
    for(auto i : mp) {
        cout << i.second << "\t";
    }
    cout << endl << "----------------" << endl;
    for(auto i : hsmooth) {
        cout << i.first << "\t";
    }
    cout << endl;
    for(auto i : hsmooth) {
        cout << i.second << "\t";
    }
    return 0;
}

/*
6 6
1 2 1 3 2 1
4 4 3 2 4 0
6 9 2 3 2 1
6 2 0 5 3 0
3 4 0 5 1 5
5 6 8 9 3 6
3 or 5
*/