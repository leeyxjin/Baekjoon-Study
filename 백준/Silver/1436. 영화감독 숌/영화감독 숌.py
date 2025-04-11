user=int(input())
ls=[]
num=0
while True:
    if len(ls)==10000: break
    else:
        num+=1
        num_ls=str(num).split('666')
        num_new=''
        for i in num_ls:
            num_new+=str(i)
        if num_new!=str(num): ls.append(num)
print(ls[user-1])