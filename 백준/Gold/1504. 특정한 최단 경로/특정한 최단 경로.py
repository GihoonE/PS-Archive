import sys, heapq
from collections import deque
V,E = map(int,sys.stdin.readline().split())
dp = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    dp[u].append((v,w))
    dp[v].append((u,w))

s1,s2 = map(int,sys.stdin.readline().split())

dist1 = [float('inf')]*(V+1)
distX = [float('inf')]*(V+1)
distY = [float('inf')]*(V+1)
dist1[1] = 0
distX[s1] = 0
distY[s2] = 0
q = []
heapq.heappush(q,(0,1))
while q:
    dis,cur = heapq.heappop(q)
    for v,w in dp[cur]:
        if dis+w < dist1[v]:
            dist1[v] = dist1[cur]+w
            heapq.heappush(q,(dist1[v],v))

q = []
heapq.heappush(q,(0,s1))
while q:
    dis,cur = heapq.heappop(q)
    for v,w in dp[cur]:
        if dis+w < distX[v]:
            distX[v] = distX[cur]+w
            heapq.heappush(q,(distX[v],v))

q = []
heapq.heappush(q,(0,s2))
while q:
    dis,cur = heapq.heappop(q)
    for v,w in dp[cur]:
        if dis+w < distY[v]:
            distY[v] = distY[cur]+w
            heapq.heappush(q,(distY[v],v))

ans = min(dist1[s1]+distX[s2]+distY[V],dist1[s2]+distY[s1]+distX[V])
print(ans if ans < float('inf') else -1)