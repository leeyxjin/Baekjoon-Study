x=[]
for i in range(1,31):
    x.append(i)

y=[]
for i in range(28):
    y.append(int(input()))

for i in x:
    if i in y:
        pass
    else: print(i)