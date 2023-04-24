import math
def check(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return (n > 1)

def xuat(a):
    for i in a: 
        print(i, end=" ")
    print()

def solve():
    n1n2=[int(i) for i in input().split()]
    n1=n1n2[0]
    n2=n1n2[1]

    a = set([int(i) for i in input().split()])
    b = set([int(i) for i in input().split()])

    if len(a.difference(b)) == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()