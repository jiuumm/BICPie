from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
pos = PriorityQueue()
neg = PriorityQueue()
zero = False
sum = 0

for _ in range(n):
    temp = int(input())
    if temp>1:
        pos.put(temp*-1)
    elif temp<0:
        neg.put(temp)
    elif temp==1:
        sum+=1
    else:
        zero=True

while pos.qsize()>0:
    n1 = pos.get()*-1
    if pos.empty():
        sum+=n1
        break
    n2 = pos.get()*-1
    sum+=n1*n2

while neg.qsize()>0:
    n1 = neg.get()
    if neg.empty():
        if not zero:
            sum+=n1
        break
    n2 = neg.get()
    sum+=n1*n2

print(sum)
    