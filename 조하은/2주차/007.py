import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
num = list(map(int, input().split()))
num.sort()
cnt = 0
i = 0
j = n-1

while i<j:
  if num[i]+num[j]==m:
    cnt+=1
    i+=1
    j-=1
  elif num[i]+num[j]>m:
    j-=1
  else:
    i+=1
    
print(cnt)