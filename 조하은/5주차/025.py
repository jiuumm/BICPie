import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n)]
visited = [False]*(n+1)
arrive = False

def DFS(now, depth):
    global arrive
    if depth==5:
        arrive = True
        return
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i, depth+1)
    visited[now] = False

for _ in range(m):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

for i in range(n):
    DFS(i, 1)
    if arrive:
        print(1)
        exit()

print(0)