
import sys
from collections import deque
N,T = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
C = list(map(int,sys.stdin.readline().split()))
MAX_C = sum(C)
dp = [0]*(MAX_C+1)
for i in range(N):
    cur_memory = A[i]
    cur_cost = C[i]
    for j in range(MAX_C,cur_cost-1,-1):
        dp[j] = max(dp[j],dp[j-cur_cost]+cur_memory)
for i in range(len(dp)):
    if dp[i] >= T:
        print(i)
        sys.exit()