import sys
input = sys.stdin.readline

n,l = map(int, input().split())
A = list(map(int, input().split()))

min_A = A[0]
arr = []
for i in range(l):
  arr.append(A[i])
  if A[i]<min_A:
    min_A = A[i]
  print(min_A, end=' ')

for i in range(l, n):
  arr.append(A[i])
  arr.remove(arr[0])
  print(min(arr), end=' ')