import sys
input=sys.stdin.readline

while True:
    x=input()
    if not x:
        break
    a,b=map(int,x.split())
    print(a+b)