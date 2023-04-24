t = int(input())

while t > 0:
    s=input()
    n=len(s)
    str1 = s[:2]
    str2 = s[n-2:]
    if str1==str2: 
        print("YES")
    else: 
        print("NO")
    t-=1