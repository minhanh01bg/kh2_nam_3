def solve():
    n = int(input())
    a = []
    for i in range(n):
        a.append([int(j) for j in input().split()])

    tren = 0
    duoi = 0
    for i in range(n):
        for j in range(n):
            if j > i:
                tren += a[i][j]
            elif j < i:
                duoi += a[i][j]
    K = int(input())
    c = abs(tren-duoi)
    if c <= K:
        print("YES")
    else:
        print("NO")
    print(abs(tren-duoi))


if __name__ == "__main__":
    solve()
