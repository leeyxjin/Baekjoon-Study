import sys
ls=[]
for _ in range(int(input())):
    ls.append(int(sys.stdin.readline().strip()))
ls.sort()
for i in ls:
    print(i)