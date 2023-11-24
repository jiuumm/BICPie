from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
cards = PriorityQueue()
for _ in range(n):
    cards.put(int(input()))

cnt = 0
while cards.qsize()>=2:
    c1 = cards.get()
    c2 = cards.get()
    sum = c1+c2
    cnt += sum
    cards.put(sum)

print(cnt)
