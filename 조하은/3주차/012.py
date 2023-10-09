import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

stack = []
NGE = [-1]*n

for i in range(n):
  while stack != [] and A[i]>A[stack[-1]]:
    NGE[stack.pop()] = A[i]
  stack.append(i)

for i in NGE:
  print(i, end=" ")