import sys
from collections import deque
K = int(sys.stdin.readline().strip())
#dp[i][0] ith 눌렀을때 A, dp[i][1] ith 눌렀을때 B
dp = [[0,0] for _ in range(K+1)]
dp[0][0] = 1
for i in range(1,K+1):
    dp[i] = [dp[i-1][1],dp[i-1][1]+dp[i-1][0]]
print(f'{dp[K][0]} {dp[K][1]}')