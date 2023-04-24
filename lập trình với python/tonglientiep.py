import math
def Cnt():
    n= int(input())
    k = n*2
    sp = int(math.sqrt(k)) + 1
    cnt = 0
    for i in range(2,sp):
        if k % i == 0:
            X = i
            Y=k/i
            if (X + Y - 1) % 2 == 0:
                x = (X+Y-1)/2
                y = Y - x
                if(y >= 1 and y < x):
                    cnt+=1
    return cnt

if __name__ == "__main__":
    t = int(input())
    while(t!=0):
        print(Cnt())
        t-=1