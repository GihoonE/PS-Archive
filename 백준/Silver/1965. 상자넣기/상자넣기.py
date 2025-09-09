import sys
from collections import deque
N = int(sys.stdin.readline().strip())
size = list(map(int,sys.stdin.readline().split()))
# i th 상자를 고려했을때 최대로 넣을 수 있는 갯수
dp = [1]*(N)
for i in range(N):
    for j in range(i):
        if size[j] < size[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))