import sys
input = sys.stdin.readline

n = int(input())
A = [0]*n
for i in range(n):
    A[i] = int(input())

def merge_sort(A):
    if len(A) < 2:
        return A
    
    mid = len(A) // 2
    low_arr = merge_sort(A[:mid])
    high_arr = merge_sort(A[mid:])
    
    merged_arr = []
    l = h = 0
    while l<len(low_arr) and h<len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l+=1
        else:
            merged_arr.append(high_arr[h])
            h+=1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

result = merge_sort(A)
for i in result:
    print(i)