import sys
input=sys.stdin.readline

n,m=map(int,input().split())
ls=list(map(int,input().split()))

res=[0]*(n+1)
for i in range(n):
    res[i+1]=res[i]+ls[i]
for _ in range(m):
    a,b=map(int,input().split())
    print(res[b]-res[a-1])