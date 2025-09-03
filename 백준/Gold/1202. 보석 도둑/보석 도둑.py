import sys
import heapq as hp
N,K = map(int,sys.stdin.readline().strip().split())
l = [tuple(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
b = [int(sys.stdin.readline().strip()) for _ in range(K)]
l.sort(key=lambda x: x[0])
b.sort()
s = 0
i = 0
dp = []
for size in b:
    while i < N and l[i][0] <= size:
        hp.heappush(dp,-l[i][1])
        i += 1
    if dp:
        s -= hp.heappop(dp)
print(s)