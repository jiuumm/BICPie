exp = input()

A = list(exp.split('-'))
sum = [0]*len(A)

for i in range(len(A)):
    B = list(map(int, A[i].split('+')))
    for j in B:
        sum[i]+=j

answer = sum[0]
for i in range(1, len(sum)):
    answer-=sum[i]

print(answer)