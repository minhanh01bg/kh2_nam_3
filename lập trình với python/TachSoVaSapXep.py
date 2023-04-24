import re

t = int(input())
a = []
while t>0:
    s = input()
    temp = re.findall(r'\d+', s)
    res = list(map(int, temp))
    for i in res:
        a.append(i)
    t-=1
a.sort()
for i in a:
    print(i)