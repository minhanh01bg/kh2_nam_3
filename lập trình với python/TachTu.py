def solve():
    n = input()
    s=""
    for i in range(0,len(n)):
        if(n[i]==' '):
            print(s)
            s=""
        if(n[i]!=' '):
            s=s+n[i]
    print(s)
        
if __name__=="__main__":
    solve()