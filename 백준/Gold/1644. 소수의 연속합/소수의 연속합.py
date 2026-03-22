import sys
input = sys.stdin.readline
N = int(input())
c = [True] *(N+1)
c[0] = c[1] = False
for i in range(2, int(N**0.5)+1):
    if c[i]:
        c[i*i:N+1:i] = [False]*len(range(i*i,N+1,i))
nums = [i for i in range(2,N+1) if c[i]]
l = 0
count = 0
cur_sum = 0
for r in range(len(nums)):
    cur_sum += nums[r]
    while cur_sum >= N:
        if cur_sum == N:
            count += 1
        cur_sum -= nums[l]
        l += 1
print(count)