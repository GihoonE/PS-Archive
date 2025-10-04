import sys, heapq
from collections import deque
V,E = map(int,sys.stdin.readline().split())
S = int(sys.stdin.readline().strip())
dp = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    dp[u].append((v,w))

dist = [float('inf')]*(V+1)
dist[S] = 0
q = []
heapq.heappush(q,(0,S))
while q:
    dis,cur = heapq.heappop(q)
    for v,w in dp[cur]:
        if dis+w < dist[v]:
            dist[v] = dist[cur]+w
            heapq.heappush(q,(dist[v],v))

for i in range(1,V+1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])