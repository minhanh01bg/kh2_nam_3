s = input()
l = len(s)
if len(s) & 1:
    l = len(s) - 1

i = 0
a = []
while i + 2 < l or i < l:
    a.append(int(s[i:i+2]))
    i = i + 2

b = set(a)
c = []
for i in b:
    c.append(i)

d = []
for i in a:
    for j in c:
        if i == j:
            c.remove(j)
            d.append(j)

for i in d:
    dem = 0
    for j in a:
        if i == j:
            dem += 1
    print(f'{i} {dem}')
