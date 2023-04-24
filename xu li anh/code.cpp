// #include<bits/stdc++.h>
// using namespace std;
// int main(){
//     int a,b,L;
//     cin>>a>>b>>L;
//     int x[a][b];
//     double g[a][b];
//     int nm[L];
//     for(int i=0;i<L;i++) nm[i]=0;
//     for(int i=0;i<a;i++){
//         for(int j=0;j<b;j++){
//             cin>>x[i][j];
//             nm[x[i][j]]+=1;
//         }
//     }
//     double G[L];
//     for(int i=0;i<L;i++) G[i] = 0;
//     for(int i=0;i<L;i++){
//         for(int j= 0;j<=i;j++){
//             G[i] += ((double)nm[j]/(a*b));
//         }
//         G[i] *=(L-1);
//     }
//     for(int i=0;i<a;i++){
//         for(int j=0;j<b;j++){
//             cout<<round(G[x[i][j]])<<" ";
//         }
//         cout<<endl;
//     }
// }
#include <iostream>
#include<math.h>
using namespace std;
int main()
{
    int n, m, W, g;
    cin >> n >> m >> g >> W;
    int a[n][m];
    int h[g];
    for (int i = 0; i < g; i++)
    {
        h[i] = 0;
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> a[i][j];
            h[a[i][j]] += 1;
        }
    }
    for(int i = 0 ;i<g;i++) cout<<h[i]<< " ";
    cout<<endl;
    float smooth[g];
    for (int i = 0; i < g; i++)
    {
        smooth[i] = 0;
        for (int j = -(W - 1) / 2; j <= (W - 1) / 2; j++)
        {
            if (i-j < 0 || i-j >=g)
                continue;
            smooth[i] += h[i-j];
        }
        smooth[i] *= ((double) 1 / W);
        // cout<<smooth[i]<<" ";
        smooth[i] = round(smooth[i]);
    }
    for (int i = 0; i < g; i++)
    {
        cout << smooth[i] << " ";
    }
    cout<<endl;
    for(int i = 0;i<n;i++){
        for(int j = 0;j<m;j++){
            cout<<smooth[a[i][j]]<<" & ";
        }
        cout<<"\\"<<"\\";
        cout<<endl;
    }
}