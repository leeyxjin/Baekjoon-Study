import string
x=list(input())
for i in list(string.ascii_lowercase):
    if i in x:
        print(x.index(i))
    else: print('-1')