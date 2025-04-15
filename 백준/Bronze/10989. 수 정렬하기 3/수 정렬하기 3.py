import sys
input=sys.stdin.readline
res=[0]*10001

for _ in range(int(input())):
    num=int(input())
    res[num]+=1

for i in range(10001):
    if res[i]!=0:
        for _ in range(res[i]):
            print(i)