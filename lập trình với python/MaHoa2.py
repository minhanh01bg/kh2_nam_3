def solve():

    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    while True:
        k = input().split()
        d = 0
        if (int(k[0]) == 0):
            break
        K = int(k[0])

        s = k[1]
        x = ""
        for i in range(0,len(s)):
            x1 = 0
            for j in range(0,len(P)):
                if s[i] == P[j]:
                    x1 = j
            x = x+P[((x1+1+K)%28)-1]

        print("".join(reversed(x)))

if __name__ == "__main__":
    solve()