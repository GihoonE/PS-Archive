import sys
N = int(sys.stdin.readline().strip())
dp = [0]*(N+2)
T,P = [0],[0]
for _ in range(N):
    t,p = map(int,sys.stdin.readline().strip().split())
    T.append(t)
    P.append(p)

for i in range(1,N+1):
    dp[i+1] = max(dp[i+1],dp[i])
    if i + T[i] <= N+1:
        dp[i+T[i]] = max(dp[i]+P[i],dp[i+T[i]])
print(max(dp))