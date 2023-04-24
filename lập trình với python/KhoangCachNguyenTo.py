import math
a = []
def check(i):
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            return False
    return True

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

    n = int(n)

    x = int(x)
    k = 0
    i = x
    while True:
        print(i+a[k],end=" ")
        i = i + a[k]
        k += 1
        if k==n+1:
            break

if __name__ == "__main__":
    # t = int(input())
    # while t!=0:
    a.append(0)
    for i in range(2,20000):
        if check(i) :
            a.append(i)
    solve()
    print("")
        # t-=1