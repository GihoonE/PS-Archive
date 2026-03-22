import sys
input = sys.stdin.readline
N = int(input())
nums = sorted(list(map(int,input().split())))
l = 0
r = N - 1
min_s = float('inf')
min_l = -1
min_r = N
while l < r:
    if nums[l] + nums[r] == 0:
        print(f'{nums[l]} {nums[r]}')
        sys.exit()
        break
    
    if abs(nums[l] + nums[r]) < min_s:
        min_l = nums[l]
        min_r = nums[r]
        min_s = abs(nums[l] + nums[r])

    if nums[l] + nums[r] > 0:
        r -= 1
        if r == l:
            r += 1
            break
    else:
        l += 1
        if r == l:
            l -= 1
            break
print(f'{min_l} {min_r}')