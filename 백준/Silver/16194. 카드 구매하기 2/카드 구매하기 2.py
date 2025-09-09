import sys
from collections import deque
tar = int(sys.stdin.readline().strip())
dp = [float('inf')]*(tar+1)
dp[0] = 0
P = list(map(int,sys.stdin.readline().split()))
for i in range(len(P)):
    price = P[i]
    card_num = i+1
    for k in range(1,len(dp)):
        if k >= card_num:
            dp[k] = min(dp[k-card_num]+price,dp[k])
print(dp[-1])