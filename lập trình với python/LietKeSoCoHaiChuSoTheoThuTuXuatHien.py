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

for i in a:
    for j in c:
        if i == j:
            print(j, end=" ")
            c.remove(j)
