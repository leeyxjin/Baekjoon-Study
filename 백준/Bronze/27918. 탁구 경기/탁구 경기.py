d=0
p=0
for _ in range(int(input())):
    x=input()
    if d-p!=2 and d-p!=-2:
        if x=='D': d+=1
        else: p+=1
print(f'{d}:{p}')