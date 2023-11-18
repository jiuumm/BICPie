import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
s = 1
e = k
result = 0

while s <= e:
    mid = (s+e)//2
    cnt = 0
    for i in range(1, n+1):
        cnt += min((mid//i), n)
    if cnt < k:
        s = mid+1
    else:
        result = mid
        e = mid-1

print(result)