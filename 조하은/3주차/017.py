A = list(input())

A = list(map(int,A))
n = len(A)
for i in range(n):
  max = i
  for j in range(i+1,n):
    if A[j]>A[max]:
      max = j
  if max != i:
    temp = A[i]
    A[i] = A[max]
    A[max] = temp

for i in A:
  print(i,end="")