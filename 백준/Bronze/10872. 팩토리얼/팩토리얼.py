x=int(input())
y=1
if x!=0:
    for i in range(1,x+1):
        y*=i
    print(y)
else: print(1)