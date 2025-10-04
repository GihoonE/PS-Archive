import sys, heapq
from collections import deque
N,M = map(int,sys.stdin.readline().split())
dp = []
for _ in range(M):
    u,v,w = map(int,sys.stdin.readline().split())
    dp.append((u,v,w))

dist = [float('inf') for _ in range(N+1)]
dist[1] = 0
for i in range(N):
    if i < N-1:
        for u,v,w in dp:
            if dist[u] != float('inf') and dist[v] > dist[u]+w:
                dist[v] = dist[u] + w
    else:
        for u,v,w in dp:
            if dist[u] != float('inf') and dist[v] > dist[u]+w:
                print(-1)
                exit()

for i in range(2,N+1):
    if dist[i] == float('inf'):
        print(-1)
    else:
        print(dist[i])