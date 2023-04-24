#include<bits/stdc++.h>
using namespace std;

long long solve(int N)
{
    long long dp[N][16]; memset(dp, 0,sizeof(dp[0][0]) * N * 16);
    for (int i = 1; i <= 9; i++)
        dp[0][i] = 1;
    for (int i = 1; i < N; i++){
        for (int j = 0; j < 10; j++){
            for (int k = 0; k < 16; k++){
                int xo = j ^ k;
                dp[i][xo] += dp[i - 1][k];
            }
        }
    }
    long long count = 0;
    for (int i = 0; i < 10; i++)
        count += dp[N - 1][i];
    return count;
}

int main(){
    int N;
    cin >> N;
    if(N == 1) cout << solve(1) + 1 << endl;
    else cout << solve(N)<< endl;
}
