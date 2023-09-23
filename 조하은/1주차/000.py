N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

for i in range(N):
    for j in range(N-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for i in range(N):
    print(arr[i])