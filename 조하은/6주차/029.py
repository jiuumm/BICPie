import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))
A.sort()

for i in targets:
    t = i
    s = 0
    e = n-1
    while s<=e:
        check = False
        mid = (s+e)//2
        if t>A[mid]:
            s = mid+1
        elif t<A[mid]:
            e = mid-1
        else:
            check = True
            break
    if check:
        print(1)
    else:
        print(0)

