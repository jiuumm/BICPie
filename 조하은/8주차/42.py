import sys
input = sys.stdin.readline

n = int(input())

def gcd(a, b):
    while b!=0:
        temp = b
        b = a%b
        a = temp
    return a

for _ in range(n):
    a, b = map(int, input().split())
    lcm = a*b//gcd(a,b)
    print(lcm)