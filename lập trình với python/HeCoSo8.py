def solve():
    N = str(input())
    k = ""
    d=0
    x=0
    for i in range(len(N)-1,0-1,-1):
        if N[i]=='1':
            x = x + pow(2,d)
        d+=1
        if d == 3:
            d = 0
            k = k + str(x)
            x = 0
    if(x!=0):
        k = k+str(x)
    print("".join(reversed(k)),end="")
if __name__ == "__main__":
    # t= int(input())
    # while t!=0:
        solve() 
        # t-=1s