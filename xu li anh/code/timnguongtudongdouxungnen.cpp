#include<bits/stdc++.h>
using namespace std;
int main(){
    int g;
    cin>>g;
    float p;
    int h[g];
    cin>>p;
    for(int i = 0;i<g;i++){
        cin>>h[i];
    }
    int dp[g];
    dp[0] = h[0];
    for(int i = 1;i<g;i++){
        dp[i] = dp[i-1] + h[i];
        cout<<"t"<<i<<" = "<<dp[i]<<" ";
    }
    cout<<endl;
    float x = p/100 * dp[g-1];
    for(int i = 0;i<g;i++){
        if(dp[i] > x){
            cout<<i<<endl;
            break;
        }
    }
}