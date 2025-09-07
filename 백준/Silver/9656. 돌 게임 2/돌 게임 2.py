import sys
N = int(sys.stdin.readline().strip())
dp = [True]*1001
dp[1],dp[3] = False,False
for i in range(4,1001):
    if not dp[i-1] or not dp[i-3]:
        continue
    else:
        dp[i] = False
if dp[N]:
    print("SK")
else:
    print("CY")