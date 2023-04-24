def nguoc(n):
    return n == n[::-1]


def solve():
    a = [int(i) for i in input().split()]
    n = a[0]
    m = a[1]
    a = []
    for i in range(n):
        s = [int(j) for j in input().split()]
        a.append(s)

    k = -1

    for i in range(n):
        for j in range(m):
            if nguoc(str(a[i][j])) and a[i][j] > 10:
                if k < a[i][j]:
                    k = a[i][j]
    if k == -1:
        print("NOT FOUND")
        return
    print(k)

    for i in range(n):
        for j in range(m):
            if a[i][j] == k:
                print(f"Vi tri [{i}][{j}]")

# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 29 28 23
# 29 77 11 19
# 16 26 24 21
# 13 25 77 77


if __name__ == "__main__":
    solve()
