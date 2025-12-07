import sys
import heapq
input = sys.stdin.readline

N, C = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]

visited = [False] * N
pq = [(0, 0)]  # cost, start node
cnt = 0
cost = 0

dist = [float('inf')] * N
dist[0] = 0

while pq:
    cur_cost, u = heapq.heappop(pq)
    if visited[u]:
        continue
    visited[u] = True
    cost += cur_cost
    cnt += 1
    
    if cnt == N:
        break

    ux, uy = points[u]
    for v in range(N):
        if not visited[v]:
            vx, vy = points[v]
            d = (ux-vx)**2 + (uy-vy)**2
            if d >= C and d < dist[v]:
                dist[v] = d
                heapq.heappush(pq, (d, v))

if cnt != N:
    print(-1)
else:
    print(cost)
