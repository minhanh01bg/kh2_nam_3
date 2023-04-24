#include<bits/stdc++.h>

#define X first
#define Y second
#define pb push_back
#define make_pair mp
#define EL printf("\n")
#define sz(A) (int) A.size()
#define FOR(i,l,r) for (int i=l;i<=r;i++)
#define FOD(i,r,l) for (int i=r;i>=l;i--)
#define faster() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define ll long long
using namespace std;

int C[5001][5];
void init(){
    C[0][0]=1;
    FOR(i, 1, 5000){
        C[i][0] = 1;
        FOR(j, 1, min(4, i)){
            C[i][j] = C[i-1][j-1] + C[i-1][j];
        }
    }
}
int n;
pair<int,int>a[5001];

int gCnt(int l, int r){
    return a[r].second - a[l-1].second;
}

ll answer() {
    ll res = 0;
    
    // a = b = c = d
    FOR(i, 1, n){
        int cnt = gCnt(i,i);
        res += C[cnt][4];
    }
    
    // c = d < a = b
    FOR(i, 1, n){
        FOR(j, i + 1, n){
            int cnt1 = gCnt(i,i);
            int cnt2 = gCnt(j,j);
            res += C[cnt1][2] * C[cnt2][2];
        }
    }

    // c < d = a = b
    FOR(c, 1, n){
        FOR(dab, c+1,n){
            int cnt_c = gCnt(c,c);
            int cnt_dab = gCnt(dab,dab);
            res += cnt_c * C[cnt_dab][3]; 
        }
    }
    
    // c < d < a = b
    FOR(c, 1, n){
        FOR(ab, c + 2, n){
            int cnt_c = gCnt(c, c);
            int cnt_d = gCnt(c + 1, ab - 1);
            int cnt_ab = gCnt(ab, ab);
            res += cnt_c * cnt_d * C[cnt_ab][2];
        }
    }

    // a = b = c < d
    FOR(abc, 1, n){
        FOR(d, abc + 1, n){
            // a + b + c > d
            if(a[abc].first * 3 <= a[d].first) continue;

            int cnt_abc = gCnt(abc, abc);
            int cnt_d = gCnt(d, d);

            res += C[cnt_abc][3] * cnt_d;
        }
    }

    // c < a = b < d
    FOR(ab, 2, n){
        int d = ab + 1;
        FOR(c, 1, ab - 1){
            while(d + 1 <= n && a[d + 1].first < a[ab].first * 2 + a[c].first){
                d += 1;
            }
            if(a[d].first < a[c].first + a[ab].first*2){
                int cnt_c = gCnt(c,c);
                int cnt_ab = gCnt(ab,ab);
                int cnt_d = gCnt(ab + 1, d);
                res += cnt_c * C[cnt_ab][2] * cnt_d;
            }
        }
    }
    //a = b < c < d
    FOR(c , 2, n){
        int d = c + 1;
        FOR(ab, 1 , c){
            while(d + 1 <= n && a[d+1].first < a[ab].first*2 + a[c].first){
                d++;
            }
            if(a[d+1].first < a[ab].first*2 + a[c].first){
                int cnt_ab = gCnt(ab,ab);
                int cnt_c = gCnt(c,c);
                int cnt_d = gCnt(c+1,d);
                res += C[cnt_ab][2] * cnt_c * cnt_d;
            }
        }   
    }
    return res;
}

void slove() {
    int n, x; cin >> n;
    map<int, int> Cnt;
    FOR(i, 0, n - 1){
        cin >> x;
        Cnt[x] += 1;
    }
    n = 0;
    for(auto [val ,cnt]:Cnt){
        a[++n] = {val, cnt};
        a[n].second += a[n-1].second;
    }
    cout << answer() << endl;
}

int32_t main() {
    faster()
    init();
    int t;  cin>>t;
    while(t--)  slove();
    return 0;
}