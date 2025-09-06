import sys
N = int(sys.stdin.readline())
dp = [[0]*15 for _ in range(15)]
for i in range(15):
    for j in range(15):
        if i == 0:
            dp[0][j] = j
        else:
            dp[i][j] = dp[i][j-1]+dp[i-1][j]

for _ in range(N):
    f = int(sys.stdin.readline().strip())
    r = int(sys.stdin.readline().strip())
    print(dp[f][r])