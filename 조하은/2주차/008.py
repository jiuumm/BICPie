import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()
cnt = 0

# 음수가 있는 경우도 고려
for i in range(n):
  a = 0
  b = n-1
  while a<b:
    if A[a]+A[b] == A[i]:
      if a!=i and b!=i:
        cnt+=1
        break
      elif a==i:
        a+=1
      elif b==i:
        b-=1
    elif A[a]+A[b]<A[i]:
      a+=1
    else:
      b-=1

print(cnt)