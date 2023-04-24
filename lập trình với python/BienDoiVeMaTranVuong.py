def solve():
    nm = [int(j) for j in input().split()]
    n, m = nm[0], nm[1]
    a = []
    for i in range(n):
        a.append([int(j) for j in input().split()])

    if n > m:
        ans = []
        x = n - m
        dem = 1
        for i in range(n):
            if i % 2 == 0 and dem <= x:
                dem += 1
                continue
            else:
                ans.append(a[i])
        n -= x
        for i in range(len(ans)):
            res = ""
            for j in range(m):
                res = res + str(ans[i][j]) + " "
            print(res)
    elif n < m:
        ans = []
        y = m - n
        for i in range(n):
            dem2 = 1
            d = []
            for j in range(m):
                if j % 2 == 1 and dem2 <= y:
                    dem2 += 1
                    continue
                else:
                    d.append(a[i][j])
            ans.append(d)
        m -= y
        for i in range(len(ans)):
            res = ""
            for j in range(m):
                res = res + str(ans[i][j]) + " "
            print(res)
    else:
        for i in range(n):
            res = ""
            for j in range(m):
                res = res + str(a[i][j]) + " "
            print(res)


if __name__ == "__main__":
    solve()
