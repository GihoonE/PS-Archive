import sys
input = sys.stdin.readline
MOD = 10**9 + 7

MAX = 10000
dp = [0] * (MAX + 1)
dp[0] = 1
dp[3] = 3
dp[6] = 13

for i in range(9, MAX + 1, 3):
    dp[i] = (5 * dp[i-3] - 3 * dp[i-6] + dp[i-9]) % MOD

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n] if n % 3 == 0 else 0)
