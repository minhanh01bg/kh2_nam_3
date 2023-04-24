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

ll StringToNum(string str){
    ll d=0;
    REP(i,str.size()-1){
        d=d*10+str[i]-'0';
    }
    return d;
}

string toString (long x) {
    string s = "";
    while (x) {
        char tmp = x%10 + '0';
        x /= 10;
        s = tmp + s;
    }
    return s;
}

string del_0 (string s) {
    string str="";
    FOR(i,0,s.size()-1){
        if(s[i]=='0') continue;
        string tmp=string(1,s[i]);
        str += tmp;
    }
    return str;
}
main() {
    string a, b;
    cin >> a >> b;
    ll numA=StringToNum(a);
    ll numB=StringToNum(b);
    ll VT = StringToNum (del_0 (toString (numA + numB))); 
    ll numA0 = StringToNum(del_0(a));
    ll numB0 = StringToNum(del_0(b));
    ll VP = numA0 + numB0;
    VT==VP ? cout<<"YES":cout<<"NO";
}