x=input()
res=0
for i in x:
    time=ord(i)-ord('A')
    if time==18: res+=7
    elif time==21: res+=8
    elif time==24 or time==25: res+=9
    else: res+=(time//3)+2
print(res+len(x))