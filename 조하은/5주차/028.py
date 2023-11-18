from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
A = [[] for _ in range(n+1)]
visited = [False]*(n+1)
distance = [0]*(n+1)

for _ in range(n):
    data = list(map(int, input().split()))
    s = data[0]
    index=1
    while True:
        e = data[index]
        if e == -1:
            break
        v = data[index+1]
        A[s].append((e,v))
        index+=2

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        node = queue.popleft()
        for i in A[node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[node] + i[1]

BFS(1)
Max = 1
for i in range(2, n+1):
    if distance[Max] < distance[i]:
        Max = i

visited = [False]*(n+1)
distance = [0]*(n+1)
BFS(Max)

print(max(distance))