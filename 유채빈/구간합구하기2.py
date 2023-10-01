#m= 질의 수
n, m = map(int, input().split())
board =[[0]*(n+1)]
합 = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    board.append([0]+[int(x) for x in input().split()])
for i in range(1, n+1):
    for j in range(1, n+1):
        합[i][j]= 합[i-1][j]+ 합[i][j-1]- 합[i-1][j-1]+ board[i][j]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = 합[x2][y2]-합[x1-1][y2]-합[x2][y1-1]+합[x1-1][y1-1]
    print(result)