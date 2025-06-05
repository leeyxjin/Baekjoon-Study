t=int(input())
ls=list(map(int,input().split()))
ls.sort()
res=0
for i in ls:
    res+=i*t
    t-=1
print(res)