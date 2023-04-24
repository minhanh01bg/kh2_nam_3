#include <iostream>

using namespace std;

int main()
{
    int m, n;
    cin >> m >> n;
    int a[m + 1][n + 1];
    for (int i = 0; i <= m; i++)
    {
        for (int j = 0; j <= n; j++)
        {
            if (i == m || j == n)
            {
                a[i][j] = 0;
            }
            else
            {
                cin >> a[i][j];
            }
        }
    }
    int k1, k2;
    cin >> k1 >> k2;
    int Mx[k1][k2];
    for (int i = 0; i < k1; i++)
    {
        for (int j = 0; j < k2; j++)
        {
            cin >> Mx[i][j];
        }
    }
    cin >> k1 >> k2;
    int My[k1][k2];
    for (int i = 0; i < k1; i++)
    {
        for (int j = 0; j < k2; j++)
        {
            cin >> My[i][j];
        }
    }
    int Gx[m + 1][n + 1];
    int Gy[m + 1][n + 1];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            Gx[i][j] = 0;
            Gy[i][j] = 0;
            for (int k = 0; k < k1; k++)
            {
                for (int l = 0; l < k2; l++)
                {
                    Gx[i][j] += Mx[k][l] * a[i + k][j + l];
                    Gy[i][j] += My[k][l] * a[i + k][j + l];
                }
            }
        }
    }
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << Gx[i][j] << " ";
        }
        cout << endl;
    }
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << Gy[i][j] << " ";
        }
        cout << endl;
    }
}

/*
6 6
0 0 0 0 0 0
0 0 0 0 0 0
1 1 1 1 0 0
1 1 1 1 0 0
2 2 1 1 0 0
3 2 1 1 0 0
2 2
-1 0
0 1
2 2
0 -1
1 0
*/