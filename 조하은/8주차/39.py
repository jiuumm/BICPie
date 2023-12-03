import math
n = int(input())

def isPalindrome(n):
    num = str(n)
    s = 0
    e = len(num)-1
    while s<e:
        if num[s]==num[e]:
            s+=1
            e-=1
        else:
            return False
    return True

prime = [0]*(10000001)
for i in range(2, 10000001):
    prime[i] = i

for i in range(2, int(math.sqrt(10000001))+1):
    if prime[i] == 0:
        continue
    for j in range(2*i, 10000001, i):
        prime[j] = 0

for i in range(n, 10000001):
    if prime[i]==0:
        continue
    if isPalindrome(prime[i]):
        print(prime[i])
        break