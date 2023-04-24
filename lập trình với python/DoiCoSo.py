def changeNumber(n,k):
    s = ""
    while n > 0:
        m = n % k
        if k > 10:
            if m>=10:
                s = s + str(chr(55 + m))
            else:
                s = s + str(m)
        else:
            s = s + str(m)
        n = int(n/k)
    return "".join(reversed(s))
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
    print(changeNumber(a,b))

if __name__ == "__main__":
    t = int(input())
    while t!=0:
        solve()
        t-=1