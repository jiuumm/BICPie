import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

def qsort(start, end, k):
    global A
    if start < end:
        pivot = partition(start, end)
        if pivot==k:
            return
        elif k < pivot:
            qsort(start, pivot-1, k)
        else:
            qsort(pivot+1, end, k)

def swap(i, j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(start, end):
    global A
    if start+1==end:
        if A[start] > A[end]:
            swap(start, end)
        return end
    
    m = (start+end)//2
    swap(start, m)
    pivot = A[start]
    i = start+1
    j = end

    while i<= j:
        while pivot < A[j] and j>0:
            j = j-1
        while pivot > A[j] and i<len(A)-1:
            i = i+1
        if i<=j:
            swap(i, j)
            i = i+1
            j = j-1
    
    A[start] = A[j]
    A[j] = pivot
    return j

qsort(0, n-1, k-1)
print(A[k-1])
