import math
m, n = map(int, input().split())

num = [0]*(n+1)
for i in range(2, n+1):
    num[i] = i

for i in range(2, int(math.sqrt(n))+1):
    if num[i] == 0:
        continue
    for j in range(i*2, n+1, i):
        num[j] = 0

for i in range(m,n+1):
    if num[i] != 0:
        print(num[i])