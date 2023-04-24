s = input()
a = ""
K = ""
N = ""
d = 0
for i in range(0,len(s)):
    if (s[i] ==' '):
        d=i+1
        break
    a = a + s[i]

for i in range(d,len(s)):
    if (s[i] ==' '):
        d=i+1
        break
    K =K + s[i]

for i in range(d,len(s)):
    if (s[i] ==' '):
        break
    N = N + s[i]

dem = 0
A = int(a)
k = int(K)
for i in range(int(A/k)+1,int(N)):
    if k*i > int(N): 
        break
    print(k*i-A, end=" ")
    dem = 1
if(dem == 0): 
    print("-1")