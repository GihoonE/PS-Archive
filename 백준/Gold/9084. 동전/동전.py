import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    coin = list(map(int,sys.stdin.readline().strip().split()))
    tar = int(sys.stdin.readline().strip())
    dp = [0]*(10000+1)
    for c in coin:
        dp[c] += 1
        for i in range(c,tar+1):
            dp[i] += dp[i-c]
    print(dp[tar])