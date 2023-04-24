#include <bits/stdc++.h>
#define int long long

using namespace std;
const int maxn = 5010;
int a[maxn], dem[maxn], g[maxn], f[maxn];

int C(int n, int k)
{
    int ans1 = 1, ans2 = 1;
    for (int i = 0; i < k; i++)
        ans1 *= (n - i);
    for (int i = 2; i <= k; i++)
        ans2 *= i;
    return ans1 / ans2;
}

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        for (int i = 1; i <= n; i++)
            cin >> a[i];
        sort(a + 1, a + n + 1);
        int cnt = 0, last = -1;
        for (int i = 1; i <= n; i++)
        {
            if (a[i] != last)
                a[++cnt] = a[i], last = a[i], dem[cnt] = 1;
            else
                ++dem[cnt];
        }
        n = cnt;
        f[n + 1] = 0;
        for (int i = n; i; i--)
            g[i] = C(dem[i], 2), f[i] = f[i + 1] + g[i];
        int res = 0;
        for (int i = 1; i <= n; i++)
        {
            int l = 1;
            for (int j = i + 1; j <= n; j++)
            {
                while (l <= n && a[l] * 2 <= a[j] - a[i])
                    l++; // 2p
                res += f[l] * dem[i] * dem[j];
                if (l <= i)
                    res -= dem[i] * dem[j] * g[i] - dem[j] * g[i] * (dem[i] - 2) / 3;
                if (l <= j)
                    res -= dem[i] * dem[j] * g[j] - dem[i] * g[j] * (dem[j] - 2) / 3;
            }
            if (dem[i] > 1)
                res += g[i] * (dem[i] - 3) * (dem[i] - 2) / 12;
        }
        for (int i = 1; i <= n; i++)
            for (int j = i + 1; j <= n; j++)
                res += g[i] * g[j];
        cout << res << "\n";
    }
}