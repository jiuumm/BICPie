import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
cnt = 0

for _ in range(n):
    coins.append(int(input()))

for i in range(n-1, -1, -1):
    if k/coins[i]>0:        # if coins[i] <= k:
        cnt += k//coins[i]
        k %= coins[i]

print(cnt)