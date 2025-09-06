import sys
N = int(sys.stdin.readline().strip())
dp = [[0]*10 for _ in range(1001)]
#dp[n][c] n자리 수 중 c로 끝나는 숫자
dp[1] = [1]*10
for i in range(2,N+1):
    for j in range(10):
        dp[i][j] += sum(dp[i-1][0:j+1])%10_007
print(sum(dp[N])%10_007)