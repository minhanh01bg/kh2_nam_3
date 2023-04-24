def solve():
    s = [int(i) for i in input().split()]
    n = s[0]
    m = s[1]
    a = [int(i) for i in input().split()]
    cnt = [0]*(m+1)
    for i in range(0, n):
        cnt[a[i]] += 1
    Max = 0
    for i in range(0,n):
        if Max < cnt[a[i]]:
            Max = cnt[a[i]]
    k = 0
    x = 0
    for i in range(1, m+1):
        if cnt[i] > cnt[x] and cnt[i] < Max:
            x = i
    if x != 0:
        print(x)
    else:
        print("NONE")


if __name__ == "__main__":
    solve()
