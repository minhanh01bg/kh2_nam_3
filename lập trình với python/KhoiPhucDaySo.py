n = int(input())
b = []
for i in range(n):
    b.append([int(i) for i in input().split()])

if n == 2:
    x = int(b[0][1]/2)
    print(x, end=" ")
    print(x)
else:
    a = []
    for i in range(1, n-1):
        a.append(int((b[i-1][i] - b[i-1][i+1] + b[i][i+1])/2))

    x = b[0][1] - a[0]
    y = b[0][n-1] - x

    print(x, end=" ")
    for i in a:
        print(i, end=" ")
    print(y)
