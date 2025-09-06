import sys
N = int(sys.stdin.readline().strip())
#dp[n][0] = 길이 n, 마지막 자리가 0인 이친수 개수
# dp[n][1] = 길이 n, 마지막 자리가 1인 이친수 개수
dp = [[0,0] for _ in range(91)]
dp[1][1] = 1
if N >= 2:
    for i in range(2,91):
        dp[i][1] = dp[i-1][0]
        dp[i][0] = dp[i-1][1] + dp[i-1][0]
    print(sum(dp[N]))
else:
    print(sum(dp[N]))