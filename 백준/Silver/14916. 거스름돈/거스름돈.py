import sys
a = int(sys.stdin.readline().strip())
N = 100000
coin = [2,5]
dp = [0]*(N+1)
dp[2],dp[5] = 1,1
for i in range(2,N+1):
    if i == 2 or i == 5:
        continue
    q = float('inf')
    for c in coin:
        if dp[i-c] != 0:
            q = min(q,dp[i-c]+1)
    dp[i] = q

if dp[a] == 0 or dp[a] == float('inf'):
    print(-1)
else:
    print(dp[a])