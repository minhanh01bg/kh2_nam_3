#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define pi pair<int, int>
#define x first
#define y second
 
vector<pair<int, int>> x;
stack<pair<int, int>> s;
pi a[1000005];
 
int n, cnt = 0, res;
 
signed main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
 
    cin >> n;
 
    for(int i = 1; i <= n; i++){
        cin >> a[i].x >> a[i].y;
    }
 
    sort(a + 1, a + n + 1);
 
    for(int i = 1; i <= n; i++){
        while(s.size() && s.top().second <= a[i].second) s.pop();
        s.push(a[i]);
    }   
 
    while(s.size()) x.push_back(s.top()), s.pop();
    x.push_back({0, 0});
    reverse(x.begin(), x.end());
 
    for(int i = 1; i < x.size(); i++){
        res += (x[i].x - x[i - 1].x) * x[i].y;
    }
 
    cout << res;
}