def solve(n):
    a = []
    for i in range(0,n):
        x = int(input())
        a.append(x)
    a.sort()
    if a[0] == a[n-1]:
        print("BANG NHAU")
    else:
        print(a[0],end=" ")
        print(a[n-1])
if __name__ == "__main__":
    # t = int(input())
    while True:
        n= int(input())
        if n==0:
            break
        solve(n)
        # t-=1