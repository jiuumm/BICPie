import math
a, b = map(int, input().split())

prime = [0]*(10000001)
for i in range(2, 10000001):
    prime[i] = i

for i in range(2, int(math.sqrt(10000001))+1):
    if prime[i] == 0:
        continue
    for j in range(2*i, 10000001, i):
        prime[j] = 0

cnt = 0
for i in range(2, 10000001):
    if prime[i]!=0:
        x = prime[i]*prime[i]
        while x<=b:
            if x>=a:
                cnt+=1
            x*=prime[i]

print(cnt)