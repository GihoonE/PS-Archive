import sys
import heapq as hp
N = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().strip().split()))
dp = []
for x in arr:
    hp.heappush(dp,x)
for _ in range(N-1):
    arr = list(map(int,sys.stdin.readline().strip().split()))
    for x in arr:
        if dp[0] < x:
            hp.heappush(dp,x)
            hp.heappop(dp)
print(hp.heappop(dp))