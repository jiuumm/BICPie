n, m= map(int, input().split())
#���ӵ� �κ��� ���� m���� ���� �������� ������ ����?
lst = list(map(int, input().split()))
sm = [0]*n
sm[0]= lst[0]
for i in range(1, n):
    sm[i]= sm[i-1]+lst[i]
c=[0]*m
answer=0
for i in range(n):
    remainder = sm[i]%m
    #m���� ���� �������� answer�� 1���ϱ�
    if remainder  == 0:
        answer+=1
    c[remainder]+=1
for i in range(m):
    if c[i]>1:
        #2�� ���ջ̱�
        answer+=(c[i]*(c[i]-1)//2)
