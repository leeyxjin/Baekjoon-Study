head=int(input())
Tshirts=list(map(int, input().split()))
t,p=map(int,input().split())
order_t=0
for i in Tshirts:
    order_t+=(i//t)+1 if i%t!=0 else i//t
print(order_t)
print(head//p,head%p)