x=1
for _ in range(3):
    x*=int(input())
import string
for i in list(string.digits):
    print(list(str(x)).count(i))