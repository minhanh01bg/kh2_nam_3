import re


def solve():
    z = [int(i) for i in input().split()]
    n = z[0]
    k = z[1]
    a = []
    str2 = []
    for i in range(0, n):
        s = input()
        s = re.sub(r"[^a-zA-Z0-9]", " ", s)
        s = s.lower()

        x = s.split()
        for i in x:
            a.append(i)

    for i in a:
        if i not in str2:
            str2.append(i)
    # str2 =set(a)
    b = []
    cnt = -1
    for i in range(0, len(str2)):
        b.append([str2[i], a.count(str2[i])])
        cnt = max(a.count(str2[i]), cnt)

    b = sorted(b, key=lambda item: (cnt - item[1], item[0]), reverse=False)
    for a, c in b:
        if c >= k:
            print(a + " " + str(c))


if __name__ == "__main__":
    solve()
