x=input()
y=[]
y.append(x[0])
for i in range(1,len(x)):
    if x[i-1]!=x[i]:
        y.append(x[i])
print(''.join(y))