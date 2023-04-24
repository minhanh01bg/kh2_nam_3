#include<algorithm>
#include<cstdio>
#define MAX   800800
#define FOR(i,a,b) for (int i=(a);i<=(b);i=i+1)
#define fi   first
#define se   second
using namespace std;
typedef pair<int,int> ii;
int n;
ii a[MAX];
bool cmp(const ii &a,const ii &b) {
    return (a.fi-a.se<b.fi-b.se);
}
void init(void) {
    scanf("%d",&n);
    FOR(i,1,2*n) {
        scanf("%d",&a[i].fi);
        scanf("%d",&a[i].se);
    }
    sort(a+1,a+2*n+1,cmp);
}
void process(void) {
    int res=0;
    FOR(i,1,n) res+=a[i].fi;
    FOR(i,n+1,2*n) res+=a[i].se;
    printf("%d",res);
}
int main(void) {
    // freopen("ACM.INP","r",stdin);
    // freopen("ACM.OUT","w",stdout);
    init();
    process();
    return 0;
}