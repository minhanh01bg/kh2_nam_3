def bin_search(x, a, left_idx, right_idx):
    while left_idx <= right_idx:
        mid_idx = left_idx + (right_idx - left_idx) // 2
        mid = a[mid_idx]
        if mid == x:
            return mid_idx
        elif x < mid:
            right_idx = mid_idx - 1
        else:
            left_idx = mid_idx + 1
    return -1

a = []
for i in range(0,60):
    for j in range(0,39):
        for k in range(0,27):
            b = 2**i
            c = 3**j
            d = 5**k
            a.append(b*c*d)      

a.sort()
# print(a)
t = int(input())
while t!=0:
    t-=1
    x = int(input())
    ind = bin_search(x,a,0,len(a)-1)
    if ind!=-1:
        print(ind+1)
    else:
        print("Not in sequence")