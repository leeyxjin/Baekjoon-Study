import sys
input=sys.stdin.readline

ls=[]
def cue(x):
    global ls
    if x=='pop':
        if len(ls)!=0: print(ls.pop(0))
        else: print(-1)
    elif x=='size': print(len(ls))
    elif x=='empty':
        if len(ls)==0: print(1)
        else: print(0)
    elif x=='front':
        if len(ls)!=0: print(ls[0])
        else: print(-1)
    elif x=='back':
        if len(ls)!=0: print(ls[-1])
        else: print(-1)
    else:
        a,b=x.split()
        if a=='push':
            ls.append(int(b))
    

for _ in range(int(input())):
    cue(input().rstrip())