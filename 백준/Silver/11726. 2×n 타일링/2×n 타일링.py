import sys
N = int(sys.stdin.readline())
dp = [-1]*1001
dp[1] = 1
dp[2] = 2
def tile(a):
    if dp[a] == -1:
        dp[a] = (tile(a-1)+tile(a-2))%10_007
        return dp[a]
    else:
        return dp[a]

print(tile(N))
