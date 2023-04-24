#include <iostream>
#include<string.h>
using namespace std;
int main()
{
    int n, m;
    cin >> n >> m;
    int a[n][m];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> a[i][j];
        }
    }
    int b[n][m];
    int Max =-1000;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            b[i][j] = abs(a[i][j]-4);
            Max = max(Max,b[i][j]);
        }
    }
    int h[100];
    memset(h,0,sizeof(h));
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            h[b[i][j]] +=1;
        }
    }
    for (int i = 0; i <= Max; i++)
    {
        /* code */
        cout<<i<<" ";
    }
    cout<<endl;
    for (int i = 0; i <= Max; i++)
    {
        /* code */
        cout<<h[i]<<" ";
    }
}