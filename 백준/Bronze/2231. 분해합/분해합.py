user=int(input())
num=1
while True:
    if num<1000002:
        res=0
        num_ls=list(map(int,list(str(num))))
        num_ls.reverse()
        for i in range(len(num_ls)):
            res+=num_ls[i]*(int('1'+'0'*i)+1)
        if res==user:
            print(num)
            break
        else: num+=1
    else:
        print('0')
        break