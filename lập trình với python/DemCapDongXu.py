def binomialCoef(n, k):
    C = [[0 for x in range(k+1)] for x in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
 
    return C[n][k]
        
def solve():
    n = int(input())
    C = []
    for i in range(n):
        s = input()
        b = []
        for j in range(len(s)):
            b.append(s[j])
        C.append(b)

    cnt = 0
    ans = 0
    for i in range(0,n):
        cnt = 0
        for j in range(0,n):
            if C[i][j] =='C':
                cnt +=1

        ans += binomialCoef(cnt,2)
    
    for i in range(0,n):
        cnt = 0
        for j in range(0,n):
            if C[j][i] =='C':
                cnt += 1

        ans += binomialCoef(cnt,2)

    print(ans)
    
if __name__ == "__main__":
    solve()