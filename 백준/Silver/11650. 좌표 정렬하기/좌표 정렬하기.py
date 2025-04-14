ls=[]
for _ in range(int(input())):
    x,y=map(int,input().split())
    ls.append((x,y))

ls.sort()
for x,y in ls:
    print(x, y)