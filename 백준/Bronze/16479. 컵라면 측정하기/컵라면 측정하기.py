k=int(input())
d1,d2=map(int,input().split())

h2=k**2-((d1-d2)/2)**2
if h2==int(h2):
    print(int(h2))
else: print(h2)