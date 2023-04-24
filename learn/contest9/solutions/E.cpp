#include <bits/stdc++.h>
#define ll long long
using namespace std;
int found, m, n;
bool MAP[5005][5005];
void dfs(ll x, ll y)
{
	if (x < 0 || y < 0 || x >= m || y >= n) return;
	if (MAP[x][y] == 1) return;
	if (found) return;
	MAP[x][y] = 1;
	if (x == m - 1 && y == n - 1)
	{
		found = true;
		return;
	}
	dfs(x - 1, y);
	dfs(x, y + 1);
	dfs(x + 1, y);
	dfs(x, y - 1);
}
int main()
{
	found = false;
	cin >> m >> n;
	memset(MAP, 0, sizeof(MAP));
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			char x;
			cin >> x;
			if (x == '*') MAP[i][j] = 1;
		}
	}
	dfs(0, 0);
	if (!found)
	{
		cout << 0 << endl;
		return 0;
	}
	MAP[0][0] = 0;
	MAP[m - 1][n - 1] = 0;
	found = false;
	dfs(0, 0);
	if (!found)
	{
		cout << 1 << endl;
	}
	else
	{
		cout << 2 << endl;
	}
}
