def solve():
    n = int(input())
    C = []
    for i in range(n):
        C.append([int(j) for j in input().split()])

    ans1 = 0
    ans2 = 0
    for i in range(0, n):
        for j in range(0, n-i-1):
            ans1 += C[i][j]
        for j in range(n-i, n):
            ans2 += C[i][j]
    k = int(input())
    c = abs(ans1-ans2)
    if c <= k:
        print("YES")
    else:
        print("NO")
    print(abs(ans1-ans2))


if __name__ == "__main__":
    solve()
