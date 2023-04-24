#include <iostream>
#include <math.h>
#include <algorithm>
using namespace std;
int MaxMean(int a[], int k, int n)
{
    sort(a, a + n);
    return (a[n - 1] + a[n - 2] + a[n - 3]) / k;
}
int main()
{
    int k, theta, nmin, mmin, n, m;
    cin >> k >> theta >> nmin >> mmin >> n >> m;
    int dX[] = {0,0, 1, 0, -1, 1, -1, -1, 1};
    int dY[] = {0,1, 0, -1, 0, 1, -1, 1, -1};
    int a[n][m];
    int b[n][m];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> a[i][j];
            b[i][j] = a[i][j];
        }
    }
    for (int i = 1; i < n - 1; i++)
    {
        for (int j = 1; j < m - 1; j++)
        {
            int c[9];
            for (int k = 0; k < 9; k++)
            {
                c[k] = a[i-dX[k]][j-dY[k]];
                // cout<<c[k]<<" ";
            }
            int Max = MaxMean(c,k,9);
            // cout<<Max<<" ";
            int thetatest = abs(Max-b[i][j]);
            b[i][j] = (thetatest>theta) ? Max:b[i][j];
        }
        // cout<<endl;
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cout<<b[i][j]<<" ";
        }
        cout<<endl;
    }
}