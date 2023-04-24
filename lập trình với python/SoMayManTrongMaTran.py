NM = [int(i) for i in input().split()]
n = NM[0]
m = NM[1]
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])

lon = 0
nho = 10005

for i in range(n):
    for j in range(m):
        if a[i][j] > lon:
            lon = a[i][j]
        if a[i][j] < nho:
            nho = a[i][j]

res = lon - nho
ok = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == res:
            ok = 1
            break

if ok == 0:
    print("NOT FOUND")
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j] == res:
                print(f'Vi tri [{i}][{j}]')
