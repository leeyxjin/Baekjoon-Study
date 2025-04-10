x=[]
for _ in range(10):
    y=int(input())%42
    if y in x:
        pass
    else:
        x.append(y)
print(len(x))