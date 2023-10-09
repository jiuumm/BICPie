import sys
input = sys.stdin.readline

n = int(input())
A = []
for i in range(n):
  A.append(int(input()))

stack = []
answer = []
num = 1
for i in range(n):
  if A[i]>=num:
    while A[i]>=num:
      stack.append(num)
      num+=1
      answer.append("+")
    stack.pop()
    answer.append("-")
  else:
    p = stack.pop()
    if p > A[i]:
      break
    else:
      answer.append("-")

# 스택이 비어있으면 가능, 아니면 NO
if stack == []:
  for i in answer:
    print(i)
else:
  print("NO")