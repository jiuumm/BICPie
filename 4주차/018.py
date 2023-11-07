import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
S = [0]*n

for i in range(n):
    index = i
    key = A[i]
    for j in range(i-1,-1,-1):
        if A[j]<A[i]:
            index = j+1
            break
        if j==0:
            index = 0
    for j in range(i, index, -1):
        A[j] = A[j-1]
    A[index] = key

S[0] = A[0]
sum = S[0]
for i in range(1,n):
    S[i] = S[i-1]+A[i]
    sum+=S[i]

print(sum)