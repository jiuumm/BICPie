from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False]*(n+1)

def DFS(v):
    print(v, end=" ")    
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in A[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

for _ in range(m):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

# 번호가 작은 것부터 방문하도록 정렬
for i in range(n+1):
    A[i].sort()

DFS(v)
print()

visited = [False]*(n+1)
BFS(v)