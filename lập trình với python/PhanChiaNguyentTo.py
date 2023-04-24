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

    myset = set([])
    for i in range(0, n):
        myset.add(a[i])

    k = 0
    for i in myset:
        k += i

    myset1 = set([])
    c = 0
    cnt = 0
    check = True
    for i in range(n - 1):
        x = len(myset1)
        myset1.add(a[i])

        if len(myset1) > x:
            c += a[i]
            if isPrime(k-c) and isPrime(c):
                print(i - cnt)
                check = False
                return
        else:
            cnt += 1

    if check == True:
        print("NOT FOUND")


if __name__ == "__main__":
    solve()
