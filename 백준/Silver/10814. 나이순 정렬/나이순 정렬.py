ls=[]
for _ in range(int(input())):
    x,y=input().split()
    ls.append((int(x),y))

ls.sort(key=lambda x:x[0])
for x,y in ls:
    print(x,y)