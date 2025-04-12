a,b=map(int,input().split())
ls=[True]*1000000
ls[0]=False
for i in range(2,1001):
    if ls[i-1]:
        for j in range(i**2,1000001,i): ls[j-1]=False
for k in range(a,b+1):
    if ls[k-1]: print(k)