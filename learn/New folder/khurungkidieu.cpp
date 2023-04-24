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

string deleteSpace (string x){//a+ b -> a+b
    string rs = "";
    REP(i, x.length()-1)
        if (x[i]!=' ')
            rs+=x[i];
    return rs;
}

string delete_1 (string x) {  //delete string like (a)->a || ((a+b))->(a+b)
    stack <char> s;
    stack <int> index;
    int dele[300] = {0};
    REP(i, x.length()-1) {
        if (x[i]==')') {
            int flag = 0;
            while (s.top()!='(') {
                char top = s.top();
                if (top=='+' || top=='-')
                    flag = 1;
                s.pop();
                index.pop();
            }
            if (flag == 0) {
                dele[index.top()] = 1;
                dele[i] = 1;
            }
            s.pop();
            index.pop();
        }
        else {
            s.push(x[i]);
            index.push(i);
        }
    }
    string rs = "";
    REP(i, x.length()-1) {
        if (dele[i]==0)
            rs+=x[i];
    }
    return rs;
}

string delete_2 (string x)  {//delete string like ((a+b)+c)->(a+b+c) || (a+(b-c))->(a+b-c)
    stack <char> s;
    stack <int> index;
    int dele[300] = {0};
    REPD(i, x.length()-1) {
        if (x[i]=='(') {
            int flag = 1;
            if (i==0 || x[i-1]!='-')
                flag = 0;
            while (s.top()!=')') {
                s.pop();
                index.pop();
            }
            if (flag == 0) {
                dele[index.top()] = 1;
                dele[i] = 1;
            }
            s.pop();
            index.pop();
        }
        else {
            s.push(x[i]);
            index.push(i);
        }
    }
    string rs="";
    REP(i, x.length()-1) {
        if (dele[i]==0)
            rs+=x[i];
    }
    return rs;
}

main () {
    string str = "";
    int n;  cin>>n;
    cin.ignore();
    while (n--) {
        getline(cin, str);
        string str_no_space = deleteSpace(str);
        string str_1 = delete_1(str_no_space);
        string str_2 = delete_2(str_1);
        cout<<str_2<<endl;
    }
    return EXIT_SUCCESS;
}