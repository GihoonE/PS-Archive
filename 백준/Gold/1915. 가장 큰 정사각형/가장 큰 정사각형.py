import sys
W,H = map(int,sys.stdin.readline().split())
dp = [[0]*(H+1)]
for i in range(W):
    dp.append([0]+list(map(int,sys.stdin.readline().rstrip())))
ret = 0
for i in range(1,W+1):
    for j in range(1,H+1):
        if dp[i][j] != 0:
            dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
            ret = max(ret,dp[i][j])
        else:
            dp[i][j] = 0
print(ret*ret)