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
#define FORD2(i, a, b) for (ll i = a;i >= b; i--)
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
bool cmp1(pair<int,int>a,pair<int,int>b){
    return a.first < b.first;
}
bool cmp2(pair<int,int>a, pair<int,int>b){
    return a.second < b.second;
}
bool a[500+1], b[500+1];
pair <int, int> A[1000];
int Max=0;
int n, m, k;
void Try(int i,int d){
    if(i == k){
        Max=max(d,Max);
        return;
    }
    FOR(j,i,k-1){
        if(!a[A[j].first] && !b[A[j].second]){
            a[A[j].first] = true; b[A[j].second] = true;
            if(j==k-1){
                Max=max(d+1,Max);
                return;
            }
            d++;
            Try(i+1,d);
            d--;
            a[A[j].first]  =false; b[A[j].second] = false;
        }
    }
}

main(){
    cin >> n >> m >> k;
    FOR(i, 0, k-1){
        cin >> A[i].first>>A[i].second;
        a[A[i].first] = false;
        b[A[i].second] = false;
    }
    int d=0;
    sort(A,A+k, cmp1);
    Try(0,0);
    cout<<Max;
}