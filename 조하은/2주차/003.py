import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum = [0]

for i in range(n):
  sum.append(arr[i]+sum[i])

for i in range(m):
  s, e = map(int, input().split())
  print(sum[e]-sum[s-1])