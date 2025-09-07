import sys
T = int(sys.stdin.readline().strip())
MAX = 1_000_001
dp = [0]*MAX
n = [1,2,3]
dp[1],dp[2],dp[3] = 1,2,4
for i in range(4,MAX):
    for num in n:
        dp[i] = (dp[i]+dp[i-num])%1_000_000_009

for _ in range(T):
    a = int(sys.stdin.readline().strip())
    print(dp[a])