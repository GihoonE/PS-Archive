import sys
N,K = map(int,sys.stdin.readline().split())
dp = [10_005]*(K+1)
dp[0] = 0
coin = []
for _ in range(N):
    coin.append(int(sys.stdin.readline()))
for c in coin:
    for i in range(1,K+1):
        if i >= c:
            dp[i] = min(dp[i],dp[i-c]+1)
if dp[K] == 10_005:
    print(-1)
else:
    print(dp[K])