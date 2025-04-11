x=int(input())
y=list(map(int, input().split()))
r=0
for i in y:
    z=[]
    a=i
    for j in [2,3,5,7,11,13,17,19,23,29,31]:
        if i%j==0:
            z.append(j)
            a/=j
    for n in [2,3,5,7,11,13,17,19,23,29,31]:
        if a%n==0:
            z.append(n)
    if i==1: r+=0
    elif len(z)==0:
        r+=1
    elif len(z)==1 and z[0]==i:
        r+=1
print(r)