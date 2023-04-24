#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;
int main()
{
    int n, m, g;
    cin >> n >> m >> g;
    int a[n][m], Max = -100, h[100];
    for (int i = 0; i < g; i++)
    {
        h[i] = 0;
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> a[i][j];
            Max = max(Max, a[i][j]);
            h[a[i][j]] += 1;
        }
    }
    int tb = (n * m) / g;
    int t[100], f[100];

    t[0] = h[0];
    int cur = round(t[0] / tb) - 1;
    f[0] = max(0,cur);
    for (int i = 1; i < g; i++)
    {
        t[i] = t[i - 1] + h[i];
        cur = round(t[i] / tb) - 1;
        f[i] = max(0, cur);
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << f[a[i][j]] << " ";
        }
        cout << endl;
    }
}