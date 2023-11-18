from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
A = [[] for _ in range(n)]
visited = [[False]*m for _ in range(n)]

for i in range(n):
    str = input()
    for j in range(len(str)-1):
        A[i].append(int(str[j]))

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        node = queue.popleft()
        for k in range(4):
            x = node[0] + dx[k]
            y = node[1] + dy[k]
            if x>=0 and y>=0 and x<n and y<m:
                if A[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    A[x][y] = A[node[0]][node[1]]+1
                    queue.append((x, y))

BFS(0, 0)
print(A[n-1][m-1])