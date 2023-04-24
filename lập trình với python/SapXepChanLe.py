n=int(input())
s = input()
res = ""
res +=s
io = [int(i) for i in s.split()]
dem = len(io)
while len(io)<n:
    s = input()
    res= res + " " +s
    io = [int(i) for i in s.split()]
    dem += len(io)
    if dem==n: break

a = [int(i) for i in res.split()]
chan = []
le = []
for i in range(n):
    if(a[i]%2==1):
        le.append(a[i])
    else:
        chan.append(a[i])

x, y = 0, 0
chan.sort()
le.sort(reverse=True)

for i in range(n):
    if a[i]%2==1:
        a[i]=le[x]
        x+=1
    elif a[i]%2==0:
        a[i]=chan[y]
        y+=1

for i in a:
    print(i, end=" ")