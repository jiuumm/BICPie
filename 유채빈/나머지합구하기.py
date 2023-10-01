n, m= map(int, input().split())
#연속된 부분의 합이 m으로 나눠 떨어지는 구간의 개수?
lst = list(map(int, input().split()))
sm = [0]*n
sm[0]= lst[0]
for i in range(1, n):
    sm[i]= sm[i-1]+lst[i]
c=[0]*m
answer=0
for i in range(n):
    remainder = sm[i]%m
    #m으로 나눠 떨어지면 answer에 1더하기
    if remainder  == 0:
        answer+=1
    c[remainder]+=1
for i in range(m):
    if c[i]>1:
        #2개 조합뽑기
        answer+=(c[i]*(c[i]-1)//2)
