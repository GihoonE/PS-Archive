import sys, heapq
from collections import deque
N,M = map(int,sys.stdin.readline().split())
MAX = 100_000
dp = [float('inf')]*(MAX+1)
dp[N] = 0
q = []
heapq.heappush(q,(0,N))
while q:
    w,pos = heapq.heappop(q)
    for n_pos in (pos+1,pos-1):
        if 0 <= n_pos <= MAX:
            if dp[n_pos] > w+1:
                dp[n_pos] = w+1
                heapq.heappush(q,(w+1,n_pos))
    if 0 <= pos * 2 <= MAX:
        if dp[pos*2] > w:
            dp[pos*2] = w
            heapq.heappush(q, (w, pos*2))
print(dp[M])