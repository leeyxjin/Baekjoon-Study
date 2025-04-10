total=int(input())
volume=int(input())
sum=0
for _ in range(volume):
    a,b=map(int,input().split())
    sum+=a*b
print('Yes') if total==sum else print('No')