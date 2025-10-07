import sys, heapq
from collections import deque
N = int(sys.stdin.readline().strip())
arr = [[] for _ in range(N+1)]
visited = [-1]*(N+1)
for _ in range(N-1):
    a,b = map(int, sys.stdin.readline().strip().split())
    arr[a].append(b)
    arr[b].append(a)
visited[1] = 0
q = deque()
q.append(1)
while q:
    cur_node = q.popleft()
    for next_n in arr[cur_node]:
        if visited[next_n] == -1:
            visited[next_n] = cur_node
            q.append(next_n)
print("\n".join(map(str,visited[2:])))