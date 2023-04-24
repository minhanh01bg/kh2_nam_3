import math
def __gcd__(a,b):
    if b == 0:
        return a
    return __gcd__(b,a%b)

def sum(n):
    d = 0
    while n!=0:
        d = d + int(n%10)
        n //= 10
    return d

def isPrime(n):
    if (n<2):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
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
    a = int(n)
    b = int(x)
    k = __gcd__(a,b)
    if(isPrime(sum(k))):
        print("YES")
    else:
        print("NO"  )

if __name__ =="__main__":
    t = int(input())
    while t!=0:
        solve()
        t -=1