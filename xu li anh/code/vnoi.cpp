/**
                                        .-''-.
                                      .' .-.  )
                                     / .'  / /
    .-''` ''-.        .-''` ''-.    (_/   / /
  .'          '.    .'          '.       / /
 /              `  /              `     / /
'                ''                '   . '
|         .-.    ||         .-.    |  / /    _.-')
.        |   |   ..        |   |   ..' '  _.'.-''
 .       '._.'  /  .       '._.'  //  /.-'_.'
  '._         .'    '._         .'/    _.'
     '-....-'`         '-....-'` ( _.-'
 */
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ldb = long double;
using db = double;
using str = string; // yay python!

using pi = pair<int, int>;
using pl = pair<ll, ll>;
using pd = pair<db, db>;

using vi = vector<int>;
using vb = vector<bool>;
using vl = vector<ll>;
using vd = vector<db>;
using vs = vector<str>;
using vpi = vector<pi>;
using vpl = vector<pl>;
using vpd = vector<pd>;

// pairs
#define mp make_pair
// #define fi first
#define se second

// vectors
#define sz(x) (int)(x).size()
#define all(x) begin(x), end(x)
#define rall(x) (x).rbegin(), (x).rend()
#define sor(x) sort(all(x))
#define rsz resize
#define ins insert
#define ft front()
#define bk back()
#define pf push_front
#define pb push_back
#define eb emplace_back
#define lb lower_bound
#define ub upper_bound

#define null NULL
#define endl '\n'
// loops
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
// #define rep(i, a) rep(i, 0, a)
#define rof(i, a, b) for (int i = (b); i >= (a); --i)
#define r0f(i, a) rof(i, 0, a)
#define trav(a, x) for (auto &a : x)
#define reset(x) memset(x, 0, sizeof(x))
const int mod = 1e9 + 7;
const int MX = 5e4 + 7;
const ll INF = 1e18;
const int NM = 1e6 + 7;
const ldb PI = acos((ldb)-1);
const int dx[4] = {1, 0, -1, 0}, dy[4] = {0, 1, 0, -1}; // for every grid problem!!
/*_______________________________________MY CODE_____________________________________*/
//
// map<ll, int> f;
map<unsigned long long, unsigned long long> findA;
#define MAX 1e19
unsigned long long mul(unsigned long long a, unsigned long long b)
{
    return (a <= MAX / b) ? a * b : MAX;
}
void FindAll()
{
    unsigned long long test = 1e18;
    priority_queue<unsigned long long, vector<unsigned long long>, greater<unsigned long long>> Q;
    unsigned long long a = 1, b = 1, c = 1;
    for (int i = 0; i <= log(test) / log(2); i++)
    {
        b = 1;
        for (int j = 0; j <= log(test) / log(3); j++)
        {
            c = 1;
            for (int k = 0; k <= log(test) / log(5); k++)
            {
                unsigned long long x = mul(a, mul(b, c));
                if (x < MAX && x > 0)
                    Q.push(x);
                c = mul(c, 5);
            }
            b = mul(b, 3);
        }
        a = mul(a, 2);
    }

    int cnt = 1;
    while (!Q.empty())
    {
        findA[Q.top()] = cnt;
        cnt += 1;
        Q.pop();
    }
}

void Process()
{
    long long x;
    cin >> x;
    if (findA[x] == 0)
        cout << "Not in sequence";
    else
        cout << findA[x];
    cout << endl;
}

int32_t main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    FindAll();
    int t;
    cin >> t;
    while (t--)
    {
        Process();
    }
}
