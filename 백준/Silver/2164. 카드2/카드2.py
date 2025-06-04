from collections import deque
ls=[i+1 for i in range(int(input()))]
q=deque(ls)
while len(q)>1:
    q.popleft()
    x=q.popleft()
    q.append(x)
print(q[0])