#include <bits/stdc++.h>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N;
        cin >> N;
        if (N % 121 == 0)
            cout << "YES" << endl;
        else if (N % 12321 == 0)
            cout << "YES" << endl;
        else if (N % 1234321 == 0)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}