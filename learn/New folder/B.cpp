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
/*__________________________________________________________________*/

//tính gcd bằng thuật toán euclid

// ll gcd(ll a, ll b){
//     while(1) {
//         if(a > b) a -= b;
//         else b -= a;
//         if(a == b) return a;
//     } 
// }

// thuật toán "ngây thơ" 
//độ phức tạp: O(min(a,b))
// ll gcd(ll a, ll b){
//     FORD2(i, min(a, b), 1){
//         if(a % i == 0 && b % i == 0){
//             return i;
//         }
//     }
// }

// ll gcd(ll a, ll b){
//     if(b == 0) return a;
//     return gcd(b, a%b);
// tính chất GCD(A,B)=GCD(B,A%B) .
// }

ll lcm(ll a, ll b){
    return (a / __gcd(a, b)) * b;
}

main() {
    faster()
    ll n, k;
    run() {
        cin >> n >> k;
        ll d = n / k;
        if(d == __gcd(n * k, n + k)) {
            cout << lcm(n * k, n + k) << endl;
        }
        else cout<<"NO\n";
    }
    return EXIT_SUCCESS;
}
/*
input:
8
13 12
100 10
100056 125 
1005 125 
980 156
53 49
5 3
4 2
output:
3900
11000
NO
NO
NO
264894
120
24
----------------------------------------------------------
input:
7
23 17 
198221 198197
133649 133633
100811 100003
20051 20047 
899 546 
546 465
output:
15640
15573997670202466
4773634286681394
2024486748180462
16117888194906
709284030
NO
*/