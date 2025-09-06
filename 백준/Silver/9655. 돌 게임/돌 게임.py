import sys
N = int(sys.stdin.readline().strip())
#2개 남기면 이김
#상근(SK)이 먼저 시작 vs 창영 (CY)
dp = [False]*(N+3)
# i개 돌 남으면 이기는지-T/지는지-F
dp[1],dp[3] = True, True
for i in range(4,N+1):
    if dp[i-1] or dp[i-3]:
        dp[i] = False
    else:
        dp[i] = True
if dp[N]:
    print("SK")
else:
    print("CY")