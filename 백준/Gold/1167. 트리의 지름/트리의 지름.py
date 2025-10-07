import sys
from collections import deque
input = sys.stdin.readline
V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    for i in range(1, len(data)-1, 2):
        graph[node].append((data[i], data[i+1]))

def bfs(start):
    dist = [-1] * (V+1)
    dist[start] = 0
    q = deque([start])
    while q:
        cur = q.popleft()
        for nxt, cost in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + cost
                q.append(nxt)
    farthest_node = dist.index(max(dist))
    return farthest_node, max(dist)

node, _ = bfs(1)
_, diameter = bfs(node)
print(diameter)