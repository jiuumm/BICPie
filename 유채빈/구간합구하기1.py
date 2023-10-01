n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0, 0)
# arr 0 5 4 3 2 1
# s   0 5 9 12 14 15
# a2 = s2-s1

sum_arr = [0 for _ in range(n+1)]

for i in range(1,n+1):
    sum_arr[i]= sum_arr[i-1]+arr[i]

for i in range(m):
    a, b= map(int, input().split())
    tmp = sum_arr[b]-sum_arr[a-1]
    print(tmp)