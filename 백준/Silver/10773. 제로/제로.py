a=[]
def account(num):   #num은 int
    global a
    if num==0: del(a[-1])
    else: a.append(num)


for i in range(int(input())):
    account(int(input()))
print(sum(a))