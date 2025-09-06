import sys
N = int(sys.stdin.readline().strip())
if N%2 == 1:
    print(0)
else:
    dp = [0]*(31)
    dp[0] = 1
    dp[2] = 3
    for i in range(4,31):
        dp[i] = dp[i-2]*3
        if i%2 == 0:
            for j in range(4,i+1,2):
                dp[i] += dp[i-j]*2
    print(dp[N])