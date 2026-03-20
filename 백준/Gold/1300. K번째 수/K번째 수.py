import sys
input = sys.stdin.readline
N = int(input())
k = int(input())

l = 1
r = N**2
while l <= r:
    mid = (l+r)//2
    sum = 0
    for i in range(1,N+1):
        if N > (mid//i):
            sum += mid//i
        else:
            sum += N
    if sum >= k:
        r = mid - 1
    else:
        l = mid + 1
print(l)