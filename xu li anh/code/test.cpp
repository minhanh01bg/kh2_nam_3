#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, m1, g;
    // cin >> n >> m1 >> g;
    cin>>g;
    int a[n][m1];
    float h[g];
    for (int i = 0; i < g; i++)
        h[i] = 0;
    for (int i = 0; i < g; i++)
    {
        // for (int j = 0; j < m1; j++)
        // {
        //     cin >> a[i][j];
        //     h[a[i][j]] += 1;
        // }
        cin>>h[i];
    }

    for (int i = 0; i < g;i++){
        h[i] /= ((double)200);
    }
    float dp[g];
    dp[0] = h[0];
    for (int i = 1; i < g;i++){
        dp[i] = dp[i - 1] + h[i];
    }
    for (int i = 0; i < g;i++)
        cout << dp[i] << " ";
    cout << endl;
    float m[g];
    m[0] = 0;
    for (int i = 1; i < g;i++){
        m[i] = m[i - 1] + i * h[i];
    }
    for (int i = 0; i < g;i++)
        cout << m[i] << " ";
    cout << endl;
    
    float res[g];
    for (int i = 0; i < g;i++){
        res[i] = (double) m[g-1] * dp[i] - m[i];
        res[i] *= res[i];
        // cout << res[i] << " ";
        res[i] /= (dp[i] *  (1.0-dp[i]));
    }
    // cout << endl;
    for (int i = 0; i < g;i++)
        cout << res[i] << " ";
}
/*
6 8 10
1 4 1 1 2 3 2 3 
3 2 4 2 5 2 6 2
2 1 8 2 5 2 5 6
2 5 2 4 7 9 1 4
2 2 3 0 0 1 2 1
1 5 7 1 2 4 5 6
*/