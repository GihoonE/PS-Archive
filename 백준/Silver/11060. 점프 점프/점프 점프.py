import sys
from collections import deque
N = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
dp = [float('inf')]*(N)
dp[0] = 1
for i in range(len(dp)):
    dis = arr[i]
    for j in range(1,dis+1):
        if i+j <= N-1:
            dp[i+j] = min(dp[i+j],dp[i]+1)
if dp[N-1]-1 != float('inf'):
    print(dp[N-1]-1)
else:
    print(-1)