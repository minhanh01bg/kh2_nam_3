#include <bits/stdc++.h>

#define ll long long
#define pb push_back
#define mp make_pair
#define all(C) C.begin(), C.end()
#define run() int N; cin>>N; cin.ignore(); while(N--)

#define FOR(i,a,b) for (int i=a; i<=b; i++)
#define FOR2(i,a,b) for (ll i=a; i<=b; ++i)
#define FORD(i,a,b) for (int i=a; i>=b; i--)
#define FORA(x,C) for (auto x:C)

#define reset(C) memset(C,0,sizeof(C))
#define faster() ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define pause() system("pause");

using namespace std;

const double pi=2*acos(0);
const ll nmax=1e7+7; 

void sangUoc(vector<long> &a){
	for(long i=1;i<=nmax;i++){
		a[i]-=i;
        for(long j=1;j<=nmax/i;j++){
            a[i*j]+=i;
        }
    }
}

int main(){
	faster();
	vector<long> a(nmax,0);
	long aa, b;
	cin >> aa >> b;
	sangUoc(a);
	ll s=0;
	for (long i=aa;i<=b;i++){
		s+=abs(a[i]-i);
	}
	cout << s;
    return EXIT_SUCCESS;
}
