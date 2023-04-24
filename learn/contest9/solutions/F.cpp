/*

 * @author SangND
 * IT2 - 03
 * HUST - K63
 * -- Must try to do something for the future and someone --

				 ─────▄██▀▀▀▀▀▀▀▀▀▀▀▀▀██▄─────
				 ────███───────────────███────
				 ───███─────────────────███───
				 ──███───▄▀▀▄─────▄▀▀▄───███──
				 ─████─▄▀────▀▄─▄▀────▀▄─████─
				  ████──▄████─────████▄──█████
				 █████─██▓▓▓██───██▓▓▓██─█████
				 █████─██▓█▓██───██▓█▓██─█████
				 █████─██▓▓▓█▀─▄─▀█▓▓▓██─█████
				 ████▀──▀▀▀▀▀─▄█▄─▀▀▀▀▀──▀████
				 ███─▄▀▀▀▄────███────▄▀▀▀▄─███
				 ███──▄▀▄─█──█████──█─▄▀▄──███
				 ███─█──█─█──█████──█─█──█─███
				 ███─█─▀──█─▄█████▄─█──▀─█─███
				 ███▄─▀▀▀▀──█─▀█▀─█──▀▀▀▀─▄███
				 ████─────────────────────████
				 ─███───▀█████████████▀───████
				 ─███───────█─────█───────████
				 ─████─────█───────█─────█████
				 ───███▄──█────█────█──▄█████─
				 ─────▀█████▄▄███▄▄█████▀─────
				 ──────────█▄─────▄█──────────
				 ──────────▄█─────█▄──────────
				 ───────▄████─────████▄───────
				 ─────▄███████───███████▄─────
				 ───▄█████████████████████▄───
				 ─▄███▀───███████████───▀███▄─
				 ███▀─────███████████─────▀███
				 ▌▌▌▌▒▒───███████████───▒▒▐▐▐▐
				 ─────▒▒──███████████──▒▒─────
				 ──────▒▒─███████████─▒▒──────
				 ───────▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒───────
				 ─────────████░░█████─────────
				 ────────█████░░██████────────
				 ──────███████░░███████───────
				 ─────█████──█░░█──█████──────
				 ─────█████──████──█████──────
				 ──────████──████──████───────
				 ──────████──████──████───────
				 ──────████───██───████───────
				 ──────████───██───████───────
				 ──────████──████──████───────
				 ─██────██───████───██─────██─
				 ─██───████──████──████────██─
				 ─███████████████████████████─
				 ─██─────────████──────────██─
				 ─██─────────████──────────██─
				 ────────────████─────────────
				 ─────────────██──────────────
-  Play with me and enjoy coding...

------------------------------------------------------------------------
- *** Everything will be okay in the end
-   If it isn't okay, it isn't the end ***
			-- From someone who has been --

*/

#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <assert.h>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <numeric>
#include <chrono>
#include <random>
#include <functional>
#include <tuple>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <array>
#include <bitset>
#include <unordered_map>

#define lb lower_bound
#define up upper_bound
#define ll long long
#define ull unsigned long long
#define pb push_back
#define pob pop_back
#define fs first
#define sd second
#define gcd __gcd
#define endl "\n"
#define NDS ios_base::sync_with_stdio(false);cin.tie(0);
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<ll> vl;
typedef vector<vl> vll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

int n, m;

struct segtree{
    int size;
    vl operations;
    void init(int n){
        size = 1;
        while(size < n) size *= 2;
        operations.assign(2*size, 0LL);
    }
    void add(int l, int r, int v, int x, int lx, int rx){
        if(lx >= r || l >= rx) return ;
        if(lx >= l && rx <= r) {
            operations[x] += v;
            return;
        }
        int m = (lx + rx) / 2;
        add(l, r, v, 2 * x + 1, lx, m);
        add(l, r, v, 2 * x + 2, m, rx);
    }

    void add(int l, int r, int v){
        add(l, r, v, 0, 0, size);
    }

    ll get(int i, int x, int lx, int rx){
        if(rx - lx == 1){
            return operations[x];
        }
        int m = (lx + rx)>>1;
        ll res;
        if(i < m){
            res = get(i, 2*x + 1, lx, m);
        }
        else{
            res = get(i, 2*x + 2, m, rx);
        }
        return res + operations[x];
    }

    ll get(int i){
        return get(i, 0, 0, size);
    }

};

void solve(){
    cin >> n;
    set<ll> temp;
    vector<pll> a;
    for(int i = 0; i < n; i++){
        ll x, y;
        cin >> x >> y;
        a.pb({x, y});
        temp.insert(x);
        temp.insert(y);
    }
    int k = 0;
    map<ll, ll> ax;
    for(auto x : temp){
        ax[x] = ++k;
    }
    for(int i = 0; i < n; i++){
        a[i].first = ax[a[i].first];
        a[i].second = ax[a[i].second];
    }
    segtree st;
    st.init(2*n + 5);
    /*
    while(m--){
        int op;
        cin >> op;
        if(op == 1){
            int l, r, v;
            cin >> l >> r >> v;
            st.add(l, r, v);
        }
        else {
            int i;
            cin >> i;
            cout << st.get(i) << endl;
        }
    }*/

    for(int i = 0; i < n; i++){
        st.add(a[i].first, a[i].second + 1, 1);
    }
    ll ans = 0;
    for(int i = 0; i < 2*n; i++){
        ans = max(ans, st.get(i));
    }
    cout << ans << endl;
}

int main () {
	NDS
    solve();
}

