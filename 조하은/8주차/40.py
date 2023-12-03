import math
Min, Max = map(int, input().split())

A = [0]*(int(math.sqrt(Max))+1)
for i in range(2, int(math.sqrt(Max))+1):
    A[i] = i*i

check = [1]*(Max-Min+1)
for i in range(2, int(math.sqrt(Max))+1):
    n = Min//A[i]*A[i]
    while(n<Max+1):
        if n>=Min:
            check[n-Min] = 0
        n+=A[i]

print(sum(check))