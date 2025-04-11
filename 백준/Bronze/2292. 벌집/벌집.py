user=int(input())
i=1
j=0
while True:
    if user==1:
        print(1)
        break
    elif 1<user<8:
        print(2)
        break
    elif j<=(user-8)//6<=j+i:
        print(i+2)
        break
    else:
        j<=(user-8)//6<=j+i
        i+=1
        j+=i