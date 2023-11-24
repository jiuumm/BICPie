import sys
input = sys.stdin.readline

n = int(input())
sched = []

for _ in range(n):
    s, e = map(int, input().split())
    sched.append([e, s])
sched.sort()

cnt = 0
end = -1

for i in range(n):
    if sched[i][1] >= end:
        end = sched[i][0]
        cnt += 1

print(cnt)