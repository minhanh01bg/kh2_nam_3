#include <bits/stdc++.h>
using namespace std;
#define vi vector<int>
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
vector<vi> edge(150005);
vector<bool> visited(100005, false);
int dfs(int u)
{
    int ans = 1;
    visited[u] = true;
    FOR(i, 0, edge[u].size())
    {
        if (visited[edge[u][i]] == false)
        {
            ans += dfs(edge[u][i]);
        }
    }
    return ans;
}

int main()
{
    for (int i = 1; i < 100005; i++)
    {
        edge[i].clear();
        visited[i] = false;
    }
    int n, m;
    cin >> n >> m;
    int cnt[n + 1];
    for (int i = 1; i <= n; i++)
    {
        cnt[i] = 0;
    }
    int a, b;
    for (int i = 0; i < m; i++)
    {
        cin >> a >> b;
        edge[a].push_back(b);
        edge[b].push_back(a);
    }
    for (int i = 1; i <= n;i++){
        for (int j = 0; j < edge[i].size();j++){
            for (int k = 0; k < edge[edge[i][j]].size();k++){
                
            }
        }
    }

}