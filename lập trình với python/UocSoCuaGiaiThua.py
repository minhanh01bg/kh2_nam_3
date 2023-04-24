def solve():
    N = input()
    n = ""
    x = ""
    z = 0
    for i in range(0,len(N)):
        if(N[i]==' '):
            z = i + 1
            break
        n = n + N[i]
    for i in range(z,len(N)):
        x = x + N[i]
    a = int(n)
    b = int(x)
    cnt = 0
    while a >= b:        
        cnt += int(a/b)
        a //=b
    print(cnt)

if __name__ == "__main__":
    t = int(input())
    while t!=0:
        solve()
        t -=1