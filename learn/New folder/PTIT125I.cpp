#include <bits/stdc++.h>

#define ll long long
#define ull unsigned long long
#define pub push_back
#define pob pop_back
#define mp make_pair
#define all(C) C.begin(), C.end()
#define run() int N; cin>>N; cin.ignore(); while(N--)

#define FOR(i, a, b) for (int i = a;i <= b; i++)
#define FOR2(i, a, b) for (ll i = a;i <= b; ++i)
#define FORD(i, a, b) for (int i = a;i >= b; i--)
#define FORA(x, C) for (auto x:C)
#define REP(i, a) for(int i = 0;i <= a; i++)
#define REP2(i, a) for(ll i = 0;i <= a; i++)
#define REPD(i, a) for(int i = a;i >= 0; i--)
#define FORx(i,m,n,x)   for(int i = m; i <= n; i += x)

#define Sort(C) sort(C,C+n)
#define SORT(C) sort(c.begin(),C.end())

#define reset(C) memset(C, 0, sizeof(C))
#define faster() ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define pause() system("pause");

using namespace std;
/*__________________________________________________________________*/
main() {
    int n, k;
    cin >> n >> k;
    string number;
    cin >> number;
    stack<int>test;
    REP(i, n - 1){
        int tmp = number[i] - '0';
        if(test.empty()){
            test.push(tmp);
        }
        else {
            while(!test.empty() && tmp > test.top() && k){
                test.pop();
                k--;
            }            
            test.push(tmp);
        }
    }
    // while (k && !test.empty()) {
    //     test.pop();
    //     k--;
    // }
    vector<int> test2;
    while(!test.empty()){
        test2.push_back(test.top());
        test.pop();
    }
    for(int i = test2.size() - 1;i >= 0; i--) 
        cout<<test2[i];
}   
// int a[1201], b[1201];
// int test(int a[],int n,int b[]){
//     Sort(b);
//     int d=0,e=0;
//     int Min = 1300;
//     FOR(i,0,n-1){
//         if(a[i]==b[0]){
//             d=i;
//             FOR(j,0,n-1){
//                 if(a[j]==b[n-1]){
//                     e=j;
//                     Min=min(min(min(max(d,e)+1,max(n-d,n-e)),d+n-e+1),Min);
//                 }
//             }
//         }
//     }
//     FOR(i,0,n-1){
//         if(a[i]==b[n-1]){
//             d=i;
//             FOR(j,0,n-1){
//                 if(a[j]==b[0]){
//                     e=j;
//                     Min=min(min(min(max(d,e)+1,max(n-d,n-e)),d+n-e+1),Min);
//                 }
//             }
//         }
//     }
//     return Min;
// }
// main(){
//     run(){
//         int n;  cin >> n; 
//         REP(i,n-1){ 
//             cin >> a[i];
//             b[i]=a[i];
//         }
//         cout<<test(a,n,b)<<endl;
//     }
// }