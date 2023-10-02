import sys
input = sys.stdin.readline

s,p = map(int, input().split())
dna = input()
num = list(map(int, input().split()))
result = 0
cnt = {'A':0, 'C':0, 'G':0, 'T':0}

for i in range(p):
  cnt[dna[i]]+=1
if cnt['A']>=num[0] and cnt['C']>=num[1] and cnt['G']>=num[2] and cnt['T']>=num[3]:
    result+=1
    
for i in range(s-p):
  cnt[dna[i]]-=1
  cnt[dna[i+p]]+=1
  if cnt['A']>=num[0] and cnt['C']>=num[1] and cnt['G']>=num[2] and cnt['T']>=num[3]:
    result+=1

print(result)