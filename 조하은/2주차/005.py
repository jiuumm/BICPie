import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = list(map(int, input().split()))

sum = [0]
remainder = [0]*m
cnt = 0

for i in range(n):
  sum.append(num[i]+sum[i])
sum.remove(0)

for i in sum:
  i = i%m

for i in sum:
  if i%m ==0:
    cnt+=1
  remainder[i%m]+=1

for i in remainder:
  if i>1:
    cnt+=((i*(i-1))//2)
print(cnt)