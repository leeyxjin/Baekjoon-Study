a=int(input())
for _ in range(a):
    x=list(input().split('X'))
    y=0
    for _ in range(x.count('')):
        if '' in x:
            x.remove('')
    for i in range(len(x)):
        for j in range(len(x[i])):
            y+=j+1
    print(y)