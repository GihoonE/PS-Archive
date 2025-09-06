import sys
N = int(sys.stdin.readline().strip())
p = [0]+list(map(int,sys.stdin.readline().strip().split()))
dp = [0]*(N+1)
# i 개 살때 max price
for i in range(1,len(p)):
    for j in range(1,i+1):
        dp[i] = max(dp[i-j]+p[j],dp[i])
print(dp[N])