import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
dp = [[float('inf')] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    if c < dp[a][b]:
        dp[a][b] = c

for i in range(1, N + 1):
    dp[i][i] = 0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if dp[i][k] + dp[k][j] < dp[i][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
ans = float('inf')
for i in range(1,N+1):
    for j in range(1, N+1):
        if i != j:
            if dp[i][j] + dp[j][i] < ans:
                ans = dp[i][j] + dp[j][i]
if ans != float('inf'):
    print(ans)
else:
    print(-1)