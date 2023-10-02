import sys
input = sys.stdin.readline

n = int(input())
sum, cnt, start_index, end_index = 1, 1, 1, 1

while end_index!=n:
  if sum == n:
    cnt+=1
    end_index+=1
    sum += end_index
  elif sum > n:
    sum = sum-start_index
    start_index+=1
  else:
    end_index+=1
    sum = sum+end_index
  
print(cnt)