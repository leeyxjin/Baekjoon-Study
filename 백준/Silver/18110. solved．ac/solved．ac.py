from decimal import Decimal, ROUND_HALF_UP
import sys
input=sys.stdin.readline

num=int(input().strip())
ls=[int(input().strip()) for i in range(num)]
ls.sort()
rm=int(Decimal(str((len(ls)*0.15))).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

if num!=0:
    ls=ls[rm:len(ls)-rm]
    average=Decimal(str((sum(ls)/len(ls))))
    rounded_num = average.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    print(rounded_num)
else: print(0)