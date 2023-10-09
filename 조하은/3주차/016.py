import sys
input = sys.stdin.readline

n = int(input())
A = []
for i in range(n):
  A.append((int(input()),i))

max = 0
A.sort()
for i in range(n):
  if A[i][1]-i>max:
    max = A[i][1]-i

print(max+1)