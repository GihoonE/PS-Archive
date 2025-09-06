import sys
N,K = map(int,sys.stdin.readline().split())
dp = [0]*(K+1)
dp[0] = 1
coin = []
for _ in range(N):
    coin.append(int(sys.stdin.readline().strip()))
for c in coin:
    for j in range(c,K+1):
        dp[j] += dp[j-c]
print(dp[K])