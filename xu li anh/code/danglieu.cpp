#include<bits/stdc++.h>
using namespace std;
int main(){
    int r;
    
    cin>>r;
    float t[r];
    cin>>t[0];
    float p[r];
    for(int i = 0;i<r;i++){
        cin>>p[i];
    }
    float x = 1/2;
    for(int i  =1 ;i<r;i++){
        float x1 = 0,x2 = 0;
        for(int j = 0;j<=t[i-1];j++){
            x1 = x1 + j*p[j];
            x2 = x2 + p[j];
        }
        float y1 = 0,y2 = 0;
        for(int j = t[i-1]+1;j<r;j++){
            y1 = y1 + j*p[j];
            y2 = y2 + p[j];
        }
        t[i] = (x1/x2 + y1/y2)/2.0;
    }
    for(int i = 0;i<r;i++){
        cout<<"t"<<i<<" = "<<t[i]<<endl;
    }
}
// 10 5
// 27 45 33 22 22 36 45 34 23 13

