#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    int m, n, maxx, threshold;
    cin >> m >> n >> maxx >> threshold;
    int a[m][n];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> a[i][j];
        }
    }

    int res[m][n];
    memset(res, 0, sizeof(res));

    for (int i = 0; i < m; i++)
    {
        int u, e, b;
        for (int j = 0; j < n; j++)
        {
            if (j == 0)
                u = a[i][j];
            else
                u = a[i][j] - e;
            if (u >= threshold)
                res[i][j] = maxx;
            else
                res[i][j] = 0;
            e = res[i][j] - u;
        }
    }

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << res[i][j] << " ";
        }
        cout << endl;
    }
}