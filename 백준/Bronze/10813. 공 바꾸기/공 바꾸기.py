x,y=map(int,input().split())
ls=[]
for i in range(x):
    ls.append(str(i+1))
for _ in range(y):
    z,r=map(int,input().split())
    a=ls[z-1]
    b=ls[r-1]
    ls[z-1]=b
    ls[r-1]=a
print(' '.join(ls))