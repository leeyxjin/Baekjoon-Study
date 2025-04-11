num=int(input())
score=list(map(int, input().split()))
score.sort()
res=[i*100/score[num-1] for i in score]
print(round(sum(res)/num,6))