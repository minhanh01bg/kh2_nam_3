#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define ll long long
int n,m,x,y,z;
vector<pair<int,int>>List[100001];
priority_queue< pair<int,int> ,vector<pair<int,int>>,greater<pair<int,int>>>Q;
ll d[100001],dp[100001];

void dijstra(){
    FOR(i,1,n) d[i] = 1e18;
    d[1] = 0;
    dp[1] = 1;
    Q.push(make_pair(0,1));
    while(!Q.empty()){
        int u = Q.top().second; Q.pop();
        if(u == n){
            cout<<d[u]<<" "<<dp[u];
            return;
        }
        FOR(i,0,List[u].size()-1){
            ll v = List[u][i].second;
            ll value = List[u][i].first;
            if(d[v] > d[u] + value){
                d[v] = d[u] + value;
                dp[v] = dp[u];
                Q.push(make_pair(d[v],v));
            }
            else if(d[v] == d[u] + value)
                dp[v] += dp[u];
        }
    }
}

main(){
    cin >> n >> m;
    int k;
    FOR(i, 1, m){
        cin >> k >> x >> y >> z;
        List[x].push_back(make_pair(z, y));
        if(k == 2) List[y].push_back(make_pair(z, x));
    }
    dijstra();
    return EXIT_SUCCESS;
}
/*
input
5 6

2 1 2 6

2 1 3 7

2 2 4 2

2 3 4 9

2 3 5 3

2 4 5 2

output
10 2
--------------------------
input
3 2
1 1 2 3
2 2 3 1
output
4 1
----------------------------------
input
5 6

2 1 2 6
       
2 1 3 7

2 2 4 2

2 3 4 9

2 3 5 3

1 4 5 2
output
10 2
-----------------------
input
5 6

1 1 2 6
       
1 1 3 7

1 2 4 2

1 3 4 9

1 3 5 3

1 4 5 2
output
10 2
*/