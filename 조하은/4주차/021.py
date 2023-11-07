import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
cnt = 0

def merge_sort(start, end):
    global A, cnt
    if start < end:
        m = (start+end) // 2
        merge_sort(start, m)
        merge_sort(m+1, end)
        
        temp = []
        x, y = start, m + 1
        while x <= m and y <= end:
            if A[x] <= A[y]:
                temp.append(A[x])
                x+=1
            else:
                temp.append(A[y])
                cnt += (m - x)+1
                y+=1
        if x <= m:
            temp += A[x:m+1]
        if y <= end:
            temp += A[y:end+1]
        for i in range(len(temp)):
            A[start+i] = temp[i]

merge_sort(0, n-1)
print(cnt)