from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
que = PriorityQueue()

for i in range(n):
  tmp = int(input())
  if tmp == 0:
    if que.empty():
      print(0)
    else:
      print(que.get()[1])
  else:
    que.put((abs(tmp),tmp))