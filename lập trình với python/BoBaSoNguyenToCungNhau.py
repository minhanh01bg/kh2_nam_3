import math


def solve():
    a = [int(i) for i in input().split()]
    L = a[0]
    R = a[1]
    for i in range(L, R-1):
        for j in range(i+1, R):
            if math.gcd(i, j) == 1:
                for k in range(j+1, R+1):
                    if math.gcd(i, k) == 1 and math.gcd(j, k) == 1:
                        print(f"({i}, {j}, {k})")


if __name__ == "__main__":
    solve()
