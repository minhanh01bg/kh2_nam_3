def solve():
    n = int(input())
    a = []
    for i in range(0,n):
        x = int(input())
        a.append(x)
    
    b = [0]*10001
    for i in range(0,n):
        b[a[i]] +=1;
    
    cnt = b[a[0]]
    k = a[0]
    for i in range(1,n):
        if  cnt < b[a[i]]:
            cnt = b[a[i]]
            k = a[i]
        if  cnt == b[a[i]] and k > a[i]:
            cnt = b[a[i]]
            k = a[i]
        
    print(k)

if __name__ == "__main__":
    t = int(input())
    while t!=0:
        solve()
        t-=1