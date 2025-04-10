x=int(input())
for _ in range(x):
    a,b=input().split()
    c=list(b)
    for i in range(len(c)):
        print(c[i]*int(a),end='')
    print('')