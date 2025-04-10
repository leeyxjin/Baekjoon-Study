x=list(map(int,input().split()))
y=0
for i in range(5):
    y+=x[i]**2
print(y%10)