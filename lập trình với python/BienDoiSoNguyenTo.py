import math


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n))+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True


def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    cnt = 0
    for i in range(0, n):
        if isPrime(a[i]) == False:
            k1 = 0
            k2 = 0
            for j in range(a[i]+1, 10000):
                if(isPrime(j)):
                    k1 = j
                    break
            for j in range(a[i]-1, 1, -1):
                if isPrime(j):
                    k2 = j
                    break
            cnt = max(cnt, min(abs(k1-a[i]), abs(k2-a[i])))
    print(cnt)


if __name__ == "__main__":
    solve()
