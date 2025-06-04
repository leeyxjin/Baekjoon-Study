import sys
from collections import Counter

input = sys.stdin.readline
ls = [int(input()) for _ in range(int(input()))]

# 산술평균
def a(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    elif num - int(num) <= -0.5:
        return int(num) - 1
    else:
        return int(num)
print(a(sum(ls) / len(ls)))

# 중앙값
ls2 = sorted(ls)
print(ls2[len(ls)//2])

# 최빈값
def b(ls):
    counter = Counter(ls)
    max_freq = max(counter.values())
    most = [k for k, v in counter.items() if v == max_freq]
    most.sort()
    if len(most) == 1:
        return most[0]
    else:
        return most[1]
print(b(ls))

# 범위
print(max(ls) - min(ls))
