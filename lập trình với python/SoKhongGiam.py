def solve():
    n = input()
    for i in range(0,len(n)-1):
        if(n[i]>n[i+1]):
            print("NO")
            return
    print("YES")
if __name__ == "__main__":
    t = int(input())
    while True:
        solve()
        t-=1
        if(t==0): 
            break