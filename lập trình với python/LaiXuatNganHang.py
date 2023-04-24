import math

t = int(input())
while t>0:
    a = [float(i) for i in input().split() ]
    gui = a[0]
    lai = a[1]
    total = a[2]
    i = 0
    T = gui
    while T < total:
        T = gui*pow((1+lai/100),i)
        i+=1
    print(i-1)
    t-=1