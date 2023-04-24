def solve():
    n = input()
    k = int(n[0]) + int(n[4])
    if k == int(n[8]):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()