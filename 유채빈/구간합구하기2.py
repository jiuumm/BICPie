#m= ���� ��
n, m = map(int, input().split())
board =[[0]*(n+1)]
�� = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    board.append([0]+[int(x) for x in input().split()])
for i in range(1, n+1):
    for j in range(1, n+1):
        ��[i][j]= ��[i-1][j]+ ��[i][j-1]- ��[i-1][j-1]+ board[i][j]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = ��[x2][y2]-��[x1-1][y2]-��[x2][y1-1]+��[x1-1][y1-1]
    print(result)