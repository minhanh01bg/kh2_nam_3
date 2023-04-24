def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    cnt = 0
    idx = 0
    update = 100000000
    for i in range(0, n):
        cnt = 0
        for j in range(0, n):
            if j == i:
                continue
            cnt += abs(a[i]-a[j])
        if update > cnt:
            update = cnt
            idx = a[i]

    print(f"{update} {idx}")


if __name__ == "__main__":
    solve()
