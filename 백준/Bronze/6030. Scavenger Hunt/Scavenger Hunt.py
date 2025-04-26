a,b=map(int,input().split())

for i in range(1,a+1):
    if a%i==0:
        for j in range(1,b+1):
            if b%j==0:
                print(i,j)