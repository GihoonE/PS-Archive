import sys
input = sys.stdin.readline
N, T = map(int, input().split())
arr = list(map(int,input().split()))
up_h = max(arr)
lo_h = 0
while lo_h <= up_h:
    mid = (up_h + lo_h) // 2
    cur = 0
    for l in arr:
        if l > mid:
            cur += l-mid
        if cur >= T:
            lo_h = mid + 1
            break
    if cur < T:
        up_h = mid - 1
    
print((up_h + lo_h)//2)