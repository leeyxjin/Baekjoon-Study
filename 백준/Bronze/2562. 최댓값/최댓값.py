x=[]
try:
    while True:
        x.append(int(input()))
except EOFError:
    pass
print(max(x))
print(x.index(max(x))+1)