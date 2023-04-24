#include <iostream>
using namespace std;
int main()
{
    int n, m;
    cin >> n >> m;
    int a[n + 2][m + 2], Gx[n + 2][m + 2], Gy[n + 2][m + 2], nmin, mmin, dX[] = {0, 0, 1, 0, -1, 1, -1, -1, 1}, dY[] = {0, 1, 0, -1, 0, 1, -1, 1, -1};
    for (int i = 0; i <= n + 1; i++)
    {
        for (int j = 0; j <= m + 1; j++)
        {
            a[i][j] = 0;
            Gx[i][j] = Gy[i][j] = 0;
        }
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            cin >> a[i][j];
        }
    }
    cin >> nmin >> mmin;
    int b[nmin][mmin], c[nmin][mmin];
    for (int i = 0; i < nmin; i++)
    {
        for (int j = 0; j < mmin; j++)
        {
            cin >> b[i][j];
        }
    }
    // cin >> nmin >> mmin;
    // for (int i = 0; i < nmin; i++)
    // {
    //     for (int j = 0; j < mmin; j++)
    //     {
    //         cin >> c[i][j];
    //     }
    // }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            for (int f = 0; f < 9; f++)
            {
                Gx[i][j] += a[i - dX[f]][j - dY[f]] * b[1 - dX[f]][1 - dY[f]];
                // Gy[i][j] += a[i - dX[f]][j - dY[f]] * c[1 - dX[f]][1 - dY[f]];
            }
        }
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            cout << Gx[i][j] << " & ";
        }
        cout<<"\\";
        cout<<"\\";
        cout << endl;
    }
    // for (int i = 1; i <= n; i++)
    // {
    //     for (int j = 1; j <= m; j++)
    //     {
    //         cout << Gy[i][j] << " & ";
    //     }
    //     cout<<"\\";
    //     cout << endl;
    // }
    // for (int i = 1; i <= n; i++)
    // {
    //     for (int j = 1; j <= m; j++)
    //     {
    //         cout << Gx[i][j] + Gy[i][j] << " & ";
    //     }
    //     cout<<"\\";
    //     cout << endl;
    // }
}