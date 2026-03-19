import sys
input = sys.stdin.readline

N, T = map(int, input().split())
arr = list(map(int, input().split()))

lo_h = 0
up_h = max(arr)
ans = 0

while lo_h <= up_h:
    mid = (lo_h + up_h) // 2
    cur = 0

    for l in arr:
        if l > mid:
            cur += l - mid
            if cur >= T:
                break

    if cur >= T:
        ans = mid
        lo_h = mid + 1
    else:
        up_h = mid - 1

print(ans)