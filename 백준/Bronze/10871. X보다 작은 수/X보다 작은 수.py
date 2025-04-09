a,b=map(int, input().split())
x=list(map(int, input().split()))
y=''
for i in x:
    if i<b:
        y+=f'{i} '
print(y.rstrip())