import sys
N = int(sys.stdin.readline().strip())
T = [0]
P = [0]
for _ in range(N):
    t,p = map(int,sys.stdin.readline().strip().split())
    T.append(t)
    P.append(p)
dp = [0]*(N+2)
for i in range(1,N+1):
    dp[i] = max(dp[i-1],dp[i]) #일 안했을때
    if i+T[i] < N+2:
        dp[i+T[i]] = max(dp[i+T[i]],dp[i]+P[i])
print(max(dp))