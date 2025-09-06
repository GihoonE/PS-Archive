import sys
N = int(sys.stdin.readline().strip())
dp = [0]*(N+1)
dp[1] = 1
for i in range(2,N+1):
    q = 10**18
    k = 1
    while k**2 <= i:
        q = min(q,dp[i-k**2]+1)
        k += 1
    dp[i] = q
print(dp[N])