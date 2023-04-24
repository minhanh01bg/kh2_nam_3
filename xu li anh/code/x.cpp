#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, m;
    cin >> n >> m;
    int a[m][2];
    int cnt[n + 1];
    for (int i = 1; i <= n; i++)
    {
        cnt[i] = 0;
    }
    for (int i = 0; i < m; i++)
    {
        cin >> a[i][0] >> a[i][1];
        if (a[i][0] != a[i][1])
        {
            cnt[a[i][0]] += 1;
            cnt[a[i][1]] += 1;
        }
    }
    int check = -1;
    for (int i = 0; i < m; i++)
    {
        if (cnt[a[i][0]] != cnt[a[i][1]])
        {
            check = 0;
            break;
        }
    }
    if(check){
        cout << "YES";
    } else
        cout << "NO";
}