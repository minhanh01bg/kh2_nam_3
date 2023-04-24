def solve():
    n = input()
    for i in range(0,len(n)):
        if n[i]!='6' and n[i]!='8':
            print("NO")
            return
    if(n[0]=='8'):
        print("NO")
        return
    for i in range(0,len(n)-2):
        if n[i]=='8' and n[i+1]=='8' and n[i+2] =='8':
            print("NO")
            return

    print("YES")
        
if __name__ == "__main__":
    solve()