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


NM = [int(i) for i in input().split()]
n = NM[0]
m = NM[1]
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])

lon = 0
ok = 0
for i in range(n):
    for j in range(m):
        if isPrime(a[i][j]) and a[i][j] > lon:
            ok = 1
            lon = a[i][j]
if ok == 0:
    print("NOT FOUND")
else:
    print(lon)
    for i in range(n):
        for j in range(m):
            if a[i][j] == lon:
                print(f'Vi tri [{i}][{j}]')
